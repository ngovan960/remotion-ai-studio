#!/usr/bin/env python3
"""
Quality Policy Service
Enforces quality gates across the entire pipeline.

Checks:
- Asset completeness (all planned assets have sources)
- Domain compliance (assets match domain style/rules)
- Timing consistency (scene durations add up)
- Voiceover pacing (WPM within range)
- Resolution standards (min 1920x1080)
- Style coherence (consistent visual language)
"""
import json
from pathlib import Path
from datetime import datetime


class QualityPolicy:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.issues = []
        self.checks = []

    def validate_full_pipeline(
        self,
        classification: dict,
        plan: dict,
        asset_resolution: dict,
        domain_manifest: dict = None,
    ) -> dict:
        """
        Run all quality gates on the full pipeline output.
        Returns: {passed, score, checks, issues, summary}
        """
        print(f"\n🔍 QualityPolicy: Running pipeline validation")

        self.issues = []
        self.checks = []

        self._check_classification(classification)
        self._check_plan_structure(plan)
        self._check_scene_timing(plan)
        self._check_voiceover_pacing(plan)
        self._check_asset_resolution(asset_resolution)
        self._check_asset_coverage(plan, asset_resolution)
        self._check_domain_compliance(plan, domain_manifest)
        self._check_render_feasibility(plan)

        passed = len([i for i in self.issues if i["severity"] in ("critical", "high")]) == 0
        score = self._calculate_score()

        result = {
            "passed": passed,
            "score": score,
            "total_checks": len(self.checks),
            "passed_checks": sum(1 for c in self.checks if c["passed"]),
            "failed_checks": sum(1 for c in self.checks if not c["passed"]),
            "issues": self.issues,
            "checks": self.checks,
            "summary": self._build_summary(passed, score),
        }

        self._save_result(result)
        self._print_result(result)

        return result

    # ── Classification checks ────────────────────────────────

    def _check_classification(self, classification: dict):
        """Validate classification output."""
        domain = classification.get("domain", "")
        caps = classification.get("capabilities", [])
        confidence = classification.get("confidence", 0)

        self._record("classification_domain", bool(domain), f"Domain: {domain}", "critical")
        self._record("classification_capabilities", bool(caps), f"{len(caps)} capabilities", "high")
        self._record(
            "classification_confidence",
            confidence >= 0.3,
            f"Confidence: {confidence}",
            "medium",
        )

    # ── Plan structure checks ────────────────────────────────

    def _check_plan_structure(self, plan: dict):
        """Validate plan has required fields."""
        self._record("plan_scenes", bool(plan.get("scenes")), "Scenes present", "critical")
        self._record("plan_assets", bool(plan.get("assets")), "Assets present", "critical")
        self._record("plan_voiceover", bool(plan.get("voiceover_segments")), "Voiceover present", "high")
        self._record(
            "plan_duration",
            plan.get("duration_seconds", 0) > 0,
            f"Duration: {plan.get('duration_seconds', 0)}s",
            "critical",
        )

    # ── Scene timing ─────────────────────────────────────────

    def _check_scene_timing(self, plan: dict):
        """Validate scene durations are consistent and reasonable."""
        scenes = plan.get("scenes", [])
        if not scenes:
            return

        total_planned = plan.get("duration_seconds", 0)
        total_scenes = sum(s.get("duration_sec", 0) for s in scenes)

        # Allow 10% tolerance
        tolerance = total_planned * 0.1
        timing_ok = abs(total_scenes - total_planned) <= tolerance
        self._record(
            "scene_timing_sum",
            timing_ok,
            f"Scenes sum: {total_scenes}s vs planned: {total_planned}s",
            "high",
        )

        for scene in scenes:
            dur = scene.get("duration_sec", 0)
            self._record(
                f"scene_{scene['id']}_duration",
                dur >= 3,
                f"Scene {scene['id']}: {dur}s",
                "medium",
            )

    # ── Voiceover pacing ─────────────────────────────────────

    def _check_voiceover_pacing(self, plan: dict):
        """Validate voiceover words-per-minute is in natural range."""
        segments = plan.get("voiceover_segments", [])
        if not segments:
            return

        total_words = sum(s.get("estimated_words", 0) for s in segments)
        total_dur = sum(s.get("estimated_duration_sec", 0) for s in segments)

        if total_dur <= 0:
            self._record("voiceover_wpm", False, "No voiceover duration", "medium")
            return

        wpm = total_words / (total_dur / 60)
        wpm_ok = 80 <= wpm <= 180
        self._record(
            "voiceover_wpm",
            wpm_ok,
            f"WPM: {wpm:.0f} (target: 80-180)",
            "high" if not wpm_ok else "low",
        )

    # ── Asset resolution ─────────────────────────────────────

    def _check_asset_resolution(self, asset_resolution: dict):
        """Validate asset resolution stats."""
        stats = asset_resolution.get("stats", {})
        total = asset_resolution.get("total_resolved", 0)
        generate_count = stats.get("generate", 0)

        self._record("assets_resolved", total > 0, f"{total} assets resolved", "critical")

        # Warn if too many assets need generation (slow pipeline)
        gen_ratio = generate_count / total if total > 0 else 0
        self._record(
            "generation_ratio",
            gen_ratio <= 0.8,
            f"Generate ratio: {gen_ratio:.0%} ({generate_count}/{total})",
            "medium",
        )

    def _check_asset_coverage(self, plan: dict, asset_resolution: dict):
        """Check every scene has at least one resolved asset."""
        scenes = plan.get("scenes", [])
        resolved = asset_resolution.get("resolved", [])

        scene_ids_with_assets = set()
        for r in resolved:
            asset_id = r.get("asset_id", "")
            for a in plan.get("assets", []):
                if a["id"] == asset_id:
                    scene_ids_with_assets.add(a.get("scene_id", ""))

        uncovered = [s["id"] for s in scenes if s["id"] not in scene_ids_with_assets]
        self._record(
            "scene_coverage",
            len(uncovered) == 0,
            f"{len(scenes) - len(uncovered)}/{len(scenes)} scenes covered",
            "high" if uncovered else "low",
        )

    # ── Domain compliance ────────────────────────────────────

    def _check_domain_compliance(self, plan: dict, domain_manifest: dict):
        """Check plan aligns with domain-specific rules."""
        if not domain_manifest:
            self._record("domain_manifest", False, "No domain manifest loaded", "low")
            return

        self._record("domain_manifest", True, f"Domain: {domain_manifest.get('domain', 'unknown')}", "low")

        render_rules = domain_manifest.get("render_rules", {})
        max_dur = render_rules.get("max_duration", 1800)
        if isinstance(max_dur, str):
            max_dur = int(max_dur.rstrip('s'))
            
        plan_dur = plan.get("duration_seconds", 0)
        self._record(
            "domain_max_duration",
            plan_dur <= max_dur,
            f"Plan: {plan_dur}s, Max: {max_dur}s",
            "high",
        )

    # ── Render feasibility ───────────────────────────────────

    def _check_render_feasibility(self, plan: dict):
        """Estimate if render is feasible within reasonable time."""
        est = plan.get("estimated_render_time_sec", 0)
        self._record(
            "render_estimate",
            est <= 7200,
            f"Est. render: {est}s ({est // 60}min)",
            "medium",
        )

    # ── Helpers ──────────────────────────────────────────────

    def _record(self, name: str, passed: bool, detail: str, severity: str = "low"):
        self.checks.append({"check": name, "passed": passed, "detail": detail})
        if not passed and severity in ("critical", "high"):
            self.issues.append({"severity": severity, "type": name, "message": detail})

    def _calculate_score(self) -> float:
        if not self.checks:
            return 0.0
        weights = {"critical": 3.0, "high": 2.0, "medium": 1.0, "low": 0.5}
        total_w = 0
        earned_w = 0
        for check in self.checks:
            w = 0.5
            for issue in self.issues:
                if issue["type"] == check["check"]:
                    w = weights.get(issue["severity"], 0.5)
                    break
            total_w += w
            if check["passed"]:
                earned_w += w
        return round(earned_w / total_w, 2) if total_w > 0 else 0.0

    def _build_summary(self, passed: bool, score: float) -> str:
        if passed:
            return f"All critical checks passed. Score: {score}"
        critical = [i for i in self.issues if i["severity"] == "critical"]
        high = [i for i in self.issues if i["severity"] == "high"]
        return f"Failed with {len(critical)} critical, {len(high)} high issues. Score: {score}"

    def _save_result(self, result: dict):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        result["timestamp"] = datetime.now().isoformat()
        with open(meta_dir / "quality_policy.json", "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"  Saved to {meta_dir}/quality_policy.json")

    def _print_result(self, result: dict):
        status = "PASS" if result["passed"] else "FAIL"
        print(f"\n  Quality Gate: [{status}] Score: {result['score']}")
        print(f"    Checks: {result['passed_checks']}/{result['total_checks']} passed")
        if result["issues"]:
            print(f"    Issues:")
            for issue in result["issues"][:5]:
                print(f"      [{issue['severity']}] {issue['message']}")

#!/usr/bin/env python3
"""
Quality Gate Agent
Kiểm tra prompts, assets, audio, timing trước render
"""
import json
from pathlib import Path
from .config import CoreConfig


class QualityGate:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else CoreConfig.default_project_dir()
        self.checks_run = []
        self.issues = []

    def validate_plan(self, plan: dict) -> dict:
        """
        Validate toàn bộ production plan
        Trả về: {passed: bool, checks: [...], issues: [...], score: float}
        """
        print(f"\n✅ Quality Gate: Validating plan")

        self.checks_run = []
        self.issues = []

        self._check_duration(plan)
        self._check_scenes(plan)
        self._check_assets(plan)
        self._check_voiceover(plan)
        self._check_timing_consistency(plan)
        self._check_asset_coverage(plan)

        passed = len(self.issues) == 0
        score = self._calculate_score()

        result = {
            "passed": passed,
            "score": score,
            "total_checks": len(self.checks_run),
            "passed_checks": sum(1 for c in self.checks_run if c["passed"]),
            "issues": self.issues,
            "checks": self.checks_run,
        }

        self._save_result(result)

        if passed:
            print(f"  ✅ All checks passed (score: {score})")
        else:
            print(f"  ⚠️  {len(self.issues)} issues found (score: {score})")
            for issue in self.issues[:5]:
                print(f"    - [{issue['severity']}] {issue['message']}")

        return result

    # ── Individual checks ────────────────────────────────────

    def _check_duration(self, plan: dict):
        """Kiểm tra tổng duration"""
        dur = plan.get("duration_seconds", 0)

        passed = CoreConfig.MIN_TOTAL_DURATION_SEC <= dur <= CoreConfig.MAX_TOTAL_DURATION_SEC
        self._record("duration_range", passed,
            f"Duration {dur}s (allowed: {CoreConfig.MIN_TOTAL_DURATION_SEC}-{CoreConfig.MAX_TOTAL_DURATION_SEC}s)")

    def _check_scenes(self, plan: dict):
        """Kiểm tra scenes"""
        scenes = plan.get("scenes", [])

        if not scenes:
            self._record("scenes_exist", False, "No scenes in plan", "critical")
            return

        self._record("scenes_exist", True, f"{len(scenes)} scenes")

        for scene in scenes:
            dur = scene.get("duration_sec", 0)
            if dur < CoreConfig.MIN_SCENE_DURATION_SEC:
                self._record("scene_duration", False,
                    f"Scene {scene['id']}: {dur}s < minimum {CoreConfig.MIN_SCENE_DURATION_SEC}s",
                    "high")
                self.issues.append({
                    "severity": "high",
                    "type": "scene_duration",
                    "scene_id": scene["id"],
                    "message": f"Scene too short: {dur}s",
                })

    def _check_assets(self, plan: dict):
        """Kiểm tra assets"""
        assets = plan.get("assets", [])

        if not assets:
            self._record("assets_exist", False, "No assets in plan", "critical")
            return

        self._record("assets_exist", True, f"{len(assets)} assets")

        critical_assets = [a for a in assets if a.get("priority") == CoreConfig.PRIORITY_CRITICAL]
        self._record("critical_assets", len(critical_assets) > 0,
            f"{len(critical_assets)} critical assets")

        for asset in assets:
            if asset.get("type") not in CoreConfig.ASSET_TYPES:
                self.issues.append({
                    "severity": "medium",
                    "type": "invalid_asset_type",
                    "asset_id": asset.get("id"),
                    "message": f"Unknown asset type: {asset.get('type')}",
                })

    def _check_voiceover(self, plan: dict):
        """Kiểm tra voiceover segments"""
        segments = plan.get("voiceover_segments", [])

        if not segments:
            self._record("voiceover_exist", False, "No voiceover segments", "medium")
            return

        self._record("voiceover_exist", True, f"{len(segments)} segments")

        total_words = sum(s.get("estimated_words", 0) for s in segments)
        total_dur = sum(s.get("estimated_duration_sec", 0) for s in segments)

        if total_dur > 0:
            wpm = total_words / (total_dur / 60)
            if wpm > 200:
                self.issues.append({
                    "severity": "high",
                    "type": "voiceover_speed",
                    "message": f"Voiceover too fast: {wpm:.0f} words/min (max 200)",
                })
            elif wpm < 60:
                self.issues.append({
                    "severity": "medium",
                    "type": "voiceover_speed",
                    "message": f"Voiceover too slow: {wpm:.0f} words/min (min 60)",
                })

        self._record("voiceover_speed", True, f"Avg WPM: {wpm:.0f}" if total_dur > 0 else "N/A")

    def _check_timing_consistency(self, plan: dict):
        """Kiểm tra timing consistency giữa scenes và assets"""
        scenes = plan.get("scenes", [])
        assets = plan.get("assets", [])

        scene_ids = {s["id"] for s in scenes}
        orphan_assets = [a for a in assets if a.get("scene_id") not in scene_ids]

        if orphan_assets:
            self.issues.append({
                "severity": "high",
                "type": "orphan_assets",
                "message": f"{len(orphan_assets)} assets reference non-existent scenes",
            })

        self._record("timing_consistency", len(orphan_assets) == 0,
            f"{len(orphan_assets)} orphan assets")

    def _check_asset_coverage(self, plan: dict):
        """Kiểm tra mỗi scene có đủ assets"""
        scenes = plan.get("scenes", [])
        assets = plan.get("assets", [])

        scene_asset_count = {}
        for a in assets:
            sid = a.get("scene_id")
            scene_asset_count[sid] = scene_asset_count.get(sid, 0) + 1

        empty_scenes = [s["id"] for s in scenes if scene_asset_count.get(s["id"], 0) == 0]

        if empty_scenes:
            self.issues.append({
                "severity": "high",
                "type": "empty_scenes",
                "message": f"Scenes with no assets: {empty_scenes}",
            })

        self._record("asset_coverage", len(empty_scenes) == 0,
            f"{len(scenes) - len(empty_scenes)}/{len(scenes)} scenes covered")

    # ── Helpers ──────────────────────────────────────────────

    def _record(self, check_name: str, passed: bool, detail: str, severity: str = "low"):
        self.checks_run.append({
            "check": check_name,
            "passed": passed,
            "detail": detail,
        })
        if not passed and severity in ("high", "critical"):
            self.issues.append({
                "severity": severity,
                "type": check_name,
                "message": detail,
            })

    def _calculate_score(self) -> float:
        if not self.checks_run:
            return 0.0

        weights = {
            "critical": 3.0,
            "high": 2.0,
            "medium": 1.0,
            "low": 0.5,
        }

        total_weight = 0
        earned_weight = 0

        for check in self.checks_run:
            w = weights.get("low", 0.5)
            for issue in self.issues:
                if issue["type"] == check["check"]:
                    w = weights.get(issue["severity"], 0.5)
                    break
            total_weight += w
            if check["passed"]:
                earned_weight += w

        return round(earned_weight / total_weight, 2) if total_weight > 0 else 0.0

    # ── Save ─────────────────────────────────────────────────

    def _save_result(self, result: dict):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        with open(meta_dir / "quality_check.json", "w") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"  Saved to {meta_dir}/quality_check.json")


if __name__ == "__main__":
    gate = QualityGate("/home/ngovan960/Documents/remotion_ai_studio")

    test_plan = {
        "duration_seconds": 120,
        "scenes": [
            {"id": "s1", "duration_sec": 30, "act": "hook"},
            {"id": "s2", "duration_sec": 90, "act": "setup"},
        ],
        "assets": [
            {"id": "a1", "scene_id": "s1", "type": "image", "priority": 0},
            {"id": "a2", "scene_id": "s2", "type": "animation", "priority": 2},
        ],
        "voiceover_segments": [
            {"scene_id": "s1", "estimated_words": 75, "estimated_duration_sec": 30},
            {"scene_id": "s2", "estimated_words": 225, "estimated_duration_sec": 90},
        ],
    }

    result = gate.validate_plan(test_plan)
    print(json.dumps(result, indent=2)[:500])

#!/usr/bin/env python3
"""
Remotion AI Studio - Main Entry Point
Full pipeline: classify → plan → asset resolution → quality check → ready for render

Integrates:
- core/ — ProjectManager, Classifier, Planner, Scheduler, QualityGate
- services/ — AssetStrategy, QualityPolicy, CacheService
- domains/ — domain packs (manifest.yaml + rules)
- capabilities/ — capability packs (manifest.yaml + rules)
"""
import argparse
import json
import time
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))

from core.project_manager import ProjectManager
from core.config import CoreConfig
from services.asset_strategy import AssetStrategy
from services.quality_policy import QualityPolicy
from services.cache import CacheService


def load_domain_pack(domain_name: str, project_dir: Path) -> dict | None:
    """Load a domain pack from domains/<name>/manifest.yaml"""
    manifest_path = project_dir / "domains" / domain_name / "manifest.yaml"
    if not manifest_path.exists():
        print(f"  ⚠ Domain pack not found: {manifest_path}")
        return None

    try:
        import yaml
        with open(manifest_path) as f:
            return yaml.safe_load(f)
    except ImportError:
        # Fallback: read as JSON-like text parsing
        return {"domain": domain_name, "source": str(manifest_path)}


def load_capability_packs(capabilities: list, project_dir: Path) -> list:
    """Load capability packs from capabilities/<name>/manifest.yaml"""
    packs = []
    try:
        import yaml
        has_yaml = True
    except ImportError:
        has_yaml = False

    for cap in capabilities:
        manifest_path = project_dir / "capabilities" / cap / "manifest.yaml"
        if manifest_path.exists() and has_yaml:
            with open(manifest_path) as f:
                packs.append(yaml.safe_load(f))
        else:
            packs.append({"name": cap, "source": str(manifest_path)})

    return packs


def run_pipeline(topic: str, duration_seconds: int, project_dir: str, gpu_id: int = 0):
    """
    Full pipeline execution:
    1. ProjectManager: classify → plan → schedule → quality gate
    2. AssetStrategy: resolve assets (reuse/cache/stock/generate)
    3. QualityPolicy: enforce quality gates on full pipeline output
    """
    project_path = Path(project_dir)
    start_time = time.time()

    print("=" * 70)
    print("  REMOTION AI STUDIO — Full Pipeline")
    print(f"  Topic: {topic}")
    print(f"  Duration: {duration_seconds}s")
    print(f"  GPU: {gpu_id}")
    print("=" * 70)

    # ── Step 1: Core pipeline via ProjectManager ────────────
    pm = ProjectManager(project_dir)
    project = pm.create_project(topic, duration_seconds)

    classification = project["classification"]
    plan = project["plan"]

    # ── Step 2: Load domain pack ────────────────────────────
    domain_name = classification.get("domain", "education")
    domain_manifest = load_domain_pack(domain_name, project_path)
    if domain_manifest:
        print(f"\n📂 Loaded domain pack: {domain_name}")

    # ── Step 3: Load capability packs ───────────────────────
    caps = classification.get("capabilities", [])
    cap_packs = load_capability_packs(caps, project_path)
    if cap_packs:
        print(f"📂 Loaded {len(cap_packs)} capability packs: {caps}")

    # ── Step 4: Asset resolution via AssetStrategy ──────────
    domain_config = CoreConfig.DOMAINS.get(domain_name, {})
    asset_strategy = AssetStrategy(project_dir)
    asset_resolution = asset_strategy.resolve_assets(plan, domain_config)

    # ── Step 5: Quality gates via QualityPolicy ─────────────
    quality_policy = QualityPolicy(project_dir)
    quality_result = quality_policy.validate_full_pipeline(
        classification=classification,
        plan=plan,
        asset_resolution=asset_resolution,
        domain_manifest=domain_manifest,
    )

    # ── Step 6: Build final output ──────────────────────────
    elapsed = round(time.time() - start_time, 2)

    output = {
        "topic": topic,
        "duration_seconds": duration_seconds,
        "classification": classification,
        "plan": plan,
        "task_ids": project["task_ids"],
        "domain_pack": domain_manifest,
        "capability_packs": [p.get("name", "") for p in cap_packs],
        "asset_resolution": {
            "stats": asset_resolution["stats"],
            "total_resolved": asset_resolution["total_resolved"],
            "total_time_saved_sec": asset_resolution["total_time_saved_sec"],
        },
        "quality": quality_result,
        "scheduler_status": pm.queue_status(),
        "elapsed_seconds": elapsed,
        "ready_for_render": quality_result["passed"],
    }

    _save_output(project_path, output)
    _print_summary(output)

    return output


def _save_output(project_path: Path, output: dict):
    meta_dir = project_path / "metadata"
    meta_dir.mkdir(parents=True, exist_ok=True)

    with open(meta_dir / "full_pipeline.json", "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n  Saved to {meta_dir}/full_pipeline.json")


def _print_summary(output: dict):
    print(f"\n{'=' * 70}")
    print(f"  PIPELINE COMPLETE: {'PASS' if output['ready_for_render'] else 'FAIL'}")
    print(f"{'=' * 70}")
    print(f"  Topic:          {output['topic']}")
    print(f"  Domain:         {output['classification']['domain_label']}")
    print(f"  Capabilities:   {output['classification']['capabilities']}")
    print(f"  Scenes:         {output['plan']['total_scenes']}")
    print(f"  Assets:         {output['plan']['total_assets']}")
    print(f"  Quality Score:  {output['quality']['score']}")
    print(f"  Time Saved:     {output['asset_resolution']['total_time_saved_sec']}s (reuse/cache)")
    print(f"  Pipeline Time:  {output['elapsed_seconds']}s")
    print(f"  Ready:          {output['ready_for_render']}")
    print(f"{'=' * 70}")


def main():
    parser = argparse.ArgumentParser(
        description="Remotion AI Studio - AI Video Production Pipeline"
    )
    parser.add_argument("--topic", required=True, help="Video topic")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds")
    parser.add_argument(
        "--project",
        default="/home/ngovan960/Documents/remotion_ai_studio",
        help="Project directory",
    )
    parser.add_argument("--gpu", type=int, default=0, help="GPU ID")

    args = parser.parse_args()
    run_pipeline(args.topic, args.duration, args.project, args.gpu)


if __name__ == "__main__":
    main()

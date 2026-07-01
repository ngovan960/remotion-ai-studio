#!/usr/bin/env python3
"""
Asset Strategy Service
Priority chain: Reuse → Cache → Stock → Generate

For each asset requested by the planner:
1. Reuse: Check if identical asset exists in project (exact match)
2. Cache: Check if similar asset was previously generated (hash match)
3. Stock: Check stock sources (Unsplash, Pexels, etc.)
4. Generate: Create new asset via AI models (Flux, Wan, etc.)
"""
import json
from pathlib import Path
from datetime import datetime
from .cache import CacheService


class AssetStrategy:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.assets_dir = self.project_dir / "assets"
        self.cache = CacheService(project_dir)
        self.asset_log = []

    def resolve_assets(self, plan: dict, domain_config: dict = None) -> dict:
        """
        Resolve all assets in a production plan through the priority chain.
        Returns: {resolved: [...], stats: {reuse, cache, stock, generate}, total_time_saved}
        """
        print(f"\n📦 AssetStrategy: Resolving {plan.get('total_assets', 0)} assets")

        domain_config = domain_config or {}
        stats = {"reuse": 0, "cache": 0, "stock": 0, "generate": 0}
        time_saved = 0
        resolved = []

        for asset in plan.get("assets", []):
            result = self.resolve_one(asset, domain_config)
            resolved.append(result)
            stats[result["source"]] += 1
            if result["source"] in ("reuse", "cache"):
                time_saved += asset.get("estimated_gen_time_sec", 0)

        summary = {
            "resolved": resolved,
            "stats": stats,
            "total_resolved": len(resolved),
            "total_time_saved_sec": time_saved,
        }

        self._save_log(summary)
        self._print_stats(stats, len(resolved), time_saved)

        return summary

    def resolve_one(self, asset: dict, domain_config: dict = None) -> dict:
        """
        Resolve a single asset through the priority chain.
        Returns: {asset_id, source, path, reason}
        """
        asset_id = asset["id"]
        asset_type = asset["type"]
        scene_id = asset.get("scene_id", "")

        # 1. REUSE — exact file match in assets/
        path = self._check_reuse(asset_type, scene_id)
        if path:
            return {
                "asset_id": asset_id,
                "source": "reuse",
                "path": str(path),
                "reason": f"Exact match found: {path.name}",
                "gen_time_saved": asset.get("estimated_gen_time_sec", 0),
            }

        # 2. CACHE — hash match from previous generation
        cached = self.cache.check_cache(
            prompt=self._build_cache_key(asset),
            params={"asset_type": asset_type, "scene_id": scene_id},
        )
        if cached:
            return {
                "asset_id": asset_id,
                "source": "cache",
                "path": cached.get("file_path", ""),
                "reason": f"Cached entry hit: {cached.get('hash', '')[:8]}",
                "gen_time_saved": asset.get("estimated_gen_time_sec", 0),
            }

        # 3. STOCK — check stock sources from domain config
        stock_sources = self._get_stock_sources(asset_type, domain_config)
        if stock_sources:
            return {
                "asset_id": asset_id,
                "source": "stock",
                "path": "",
                "reason": f"Stock sources available: {', '.join(stock_sources)}",
                "gen_time_saved": 0,
            }

        # 4. GENERATE — must create new via AI
        return {
            "asset_id": asset_id,
            "source": "generate",
            "path": "",
            "reason": "No existing asset found; requires AI generation",
            "gen_time_saved": 0,
        }

    def record_generated(self, asset: dict, file_path: str):
        """Record a newly generated asset into the cache for future reuse."""
        self.cache.save_to_cache(
            prompt=self._build_cache_key(asset),
            file_path=file_path,
            params={
                "asset_type": asset.get("type", ""),
                "scene_id": asset.get("scene_id", ""),
                "source": "generate",
            },
            metadata={"asset_id": asset.get("id", "")},
        )
        print(f"  Recorded generated asset: {asset.get('id')} → {file_path}")

    # ── Reuse detection ──────────────────────────────────────

    def _check_reuse(self, asset_type: str, scene_id: str) -> Path | None:
        """Check if asset already exists in the assets directory."""
        type_dirs = {
            "image": "images",
            "video_clip": "videos",
            "audio": "audio",
            "voiceover": "audio",
            "text_overlay": "images",
            "animation": "videos",
        }
        subdir = type_dirs.get(asset_type, "images")
        asset_dir = self.assets_dir / subdir

        if not asset_dir.exists():
            return None

        # Look for scene-specific match
        for f in asset_dir.iterdir():
            if f.is_file() and scene_id.replace("scene_", "") in f.stem:
                return f

        return None

    # ── Stock source detection ───────────────────────────────

    def _get_stock_sources(self, asset_type: str, domain_config: dict) -> list:
        """Determine available stock sources for this asset type."""
        asset_strategy = domain_config.get("asset_strategy", {})
        image_sources = asset_strategy.get("image_sources", [])
        video_sources = asset_strategy.get("video_sources", [])

        if asset_type in ("image", "text_overlay", "chart", "map", "timeline"):
            return [s for s in image_sources if "stock" in s or "unsplash" in s or "pexels" in s]
        if asset_type in ("video_clip", "animation"):
            return [s for s in video_sources if "stock" in s or "footage" in s]

        return []

    # ── Cache key builder ────────────────────────────────────

    def _build_cache_key(self, asset: dict) -> str:
        """Build a deterministic cache key for an asset."""
        return f"{asset.get('type', 'unknown')}_{asset.get('scene_id', '')}_{asset.get('id', '')}"

    # ── Logging ──────────────────────────────────────────────

    def _save_log(self, summary: dict):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "stats": summary["stats"],
            "total_resolved": summary["total_resolved"],
            "total_time_saved_sec": summary["total_time_saved_sec"],
        }

        log_file = meta_dir / "asset_strategy_log.json"
        logs = []
        if log_file.exists():
            with open(log_file) as f:
                logs = json.load(f)

        logs.append(log_entry)
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)

        print(f"  Saved to {log_file}")

    def _print_stats(self: "AssetStrategy", stats: dict, total: int, time_saved: int):
        print(f"\n  Asset Resolution Summary:")
        print(f"    Reuse:    {stats['reuse']}/{total}")
        print(f"    Cache:    {stats['cache']}/{total}")
        print(f"    Stock:    {stats['stock']}/{total}")
        print(f"    Generate: {stats['generate']}/{total}")
        print(f"    Time saved: {time_saved}s")

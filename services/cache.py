#!/usr/bin/env python3
"""
Cache Service
Unified cache layer for the services layer.

Wraps the existing pipeline/cache_manager.py with additional features:
- Content-addressable storage via SHA-256
- TTL-based expiration
- Stats and cleanup
"""
import json
import hashlib
from pathlib import Path
from datetime import datetime


class CacheService:
    def __init__(self, project_dir=None, max_age_days: int = 30):
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.cache_dir = self.project_dir / "cache"
        self.cache_dir.mkdir(exist_ok=True)
        self.index_file = self.cache_dir / "services_index.json"
        self.max_age_days = max_age_days
        self.index = self._load_index()

    def _load_index(self) -> dict:
        if self.index_file.exists():
            with open(self.index_file) as f:
                return json.load(f)
        return {}

    def _save_index(self):
        with open(self.index_file, "w") as f:
            json.dump(self.index, f, indent=2, ensure_ascii=False)

    def _hash(self, key: str, params: dict = None) -> str:
        content = key
        if params:
            content += json.dumps(params, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()

    def check_cache(self, prompt: str, params: dict = None) -> dict | None:
        """Check if a prompt+params combo is cached and file still exists."""
        h = self._hash(prompt, params)

        if h not in self.index:
            return None

        entry = self.index[h]

        # TTL check
        created = datetime.fromisoformat(entry.get("created_at", datetime.now().isoformat()))
        age_days = (datetime.now() - created).days
        if age_days > self.max_age_days:
            self._remove(h)
            return None

        # File existence check
        file_path = entry.get("file_path", "")
        if file_path and not Path(file_path).exists():
            self._remove(h)
            return None

        print(f"  CacheService HIT: {h[:12]}...")
        return entry

    def save_to_cache(
        self,
        prompt: str,
        file_path: str,
        params: dict = None,
        metadata: dict = None,
    ):
        """Store a result in the cache."""
        h = self._hash(prompt, params)

        entry = {
            "hash": h,
            "prompt": prompt,
            "file_path": file_path,
            "params": params,
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat(),
            "file_size": Path(file_path).stat().st_size if Path(file_path).exists() else 0,
        }

        self.index[h] = entry
        self._save_index()
        print(f"  CacheService STORED: {h[:12]}... → {file_path}")

    def invalidate(self, prompt: str, params: dict = None):
        """Remove a specific entry from cache."""
        h = self._hash(prompt, params)
        self._remove(h)

    def get_stats(self) -> dict:
        """Return cache statistics."""
        total = len(self.index)
        total_size = sum(e.get("file_size", 0) for e in self.index.values())
        return {
            "entries": total,
            "total_size_mb": round(total_size / (1024 * 1024), 2),
            "max_age_days": self.max_age_days,
        }

    def cleanup(self) -> int:
        """Remove expired entries. Returns count of removed entries."""
        removed = 0
        now = datetime.now()
        to_remove = []

        for h, entry in self.index.items():
            created = datetime.fromisoformat(entry.get("created_at", now.isoformat()))
            age_days = (now - created).days
            if age_days > self.max_age_days:
                to_remove.append(h)

        for h in to_remove:
            self._remove(h)
            removed += 1

        print(f"  CacheService: Cleaned {removed} expired entries")
        return removed

    def clear(self):
        """Clear entire cache."""
        count = len(self.index)
        self.index = {}
        self._save_index()
        print(f"  CacheService: Cleared {count} entries")

    def _remove(self, hash_key: str):
        self.index.pop(hash_key, None)
        self._save_index()

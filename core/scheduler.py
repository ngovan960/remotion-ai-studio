#!/usr/bin/env python3
"""
Scheduler Agent
Task queue management với priority scheduling
"""
import json
import uuid
from pathlib import Path
from collections import deque
from .config import CoreConfig


class Scheduler:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else CoreConfig.default_project_dir()
        self.queue = deque()
        self.tasks = {}
        self.completed = []
        self.failed = []

    def enqueue_plan(self, plan: dict) -> list:
        """
        Chuyển production plan thành task queue
        Trả về list task IDs đã enqueue
        """
        print(f"\n📅 Scheduler: Enqueuing {plan['total_assets']} assets + {plan['total_scenes']} scenes")

        task_ids = []

        for asset in plan.get("assets", []):
            task_id = self._add_task(
                task_type="generate_asset",
                ref_id=asset["id"],
                scene_id=asset["scene_id"],
                asset_type=asset["type"],
                priority=asset["priority"],
                estimated_time=asset["estimated_gen_time_sec"],
            )
            task_ids.append(task_id)

        for segment in plan.get("voiceover_segments", []):
            task_id = self._add_task(
                task_type="generate_voiceover",
                ref_id=segment["scene_id"],
                scene_id=segment["scene_id"],
                asset_type="voiceover",
                priority=segment["priority"],
                estimated_time=segment["estimated_duration_sec"],
            )
            task_ids.append(task_id)

        self._sort_queue()
        self._save_state()

        print(f"  Total tasks: {len(task_ids)}")
        print(f"  Critical: {self._count_by_priority(CoreConfig.PRIORITY_CRITICAL)}")
        print(f"  High:     {self._count_by_priority(CoreConfig.PRIORITY_HIGH)}")
        print(f"  Medium:   {self._count_by_priority(CoreConfig.PRIORITY_MEDIUM)}")

        return task_ids

    def _add_task(self, task_type, ref_id, scene_id, asset_type, priority, estimated_time) -> str:
        task_id = str(uuid.uuid4())[:8]
        task = {
            "id": task_id,
            "type": task_type,
            "ref_id": ref_id,
            "scene_id": scene_id,
            "asset_type": asset_type,
            "priority": priority,
            "status": "pending",
            "estimated_time_sec": estimated_time,
        }
        self.tasks[task_id] = task
        self.queue.append(task_id)
        return task_id

    # ── Queue management ─────────────────────────────────────

    def _sort_queue(self):
        """Sort queue by priority (lower = higher priority)"""
        sorted_ids = sorted(
            self.queue,
            key=lambda tid: self.tasks[tid]["priority"]
        )
        self.queue = deque(sorted_ids)

    def _count_by_priority(self, priority: int) -> int:
        return sum(1 for t in self.tasks.values() if t["priority"] == priority)

    def next_task(self) -> dict | None:
        """Lấy task tiếp theo theo priority"""
        while self.queue:
            task_id = self.queue.popleft()
            task = self.tasks[task_id]
            if task["status"] == "pending":
                task["status"] = "in_progress"
                return task
        return None

    def complete_task(self, task_id: str, result: dict | None = None):
        """Đánh dấu task hoàn thành"""
        if task_id not in self.tasks:
            return

        task = self.tasks[task_id]
        task["status"] = "completed"
        task["result"] = result
        self.completed.append(task_id)

    def fail_task(self, task_id: str, error: str = ""):
        """Đánh dấu task failed"""
        if task_id not in self.tasks:
            return

        task = self.tasks[task_id]
        task["status"] = "failed"
        task["error"] = error
        self.failed.append(task_id)

    def retry_task(self, task_id: str):
        """Retry failed task"""
        if task_id in self.failed:
            task = self.tasks[task_id]
            task["status"] = "pending"
            task.pop("error", None)
            self.failed.remove(task_id)
            self.queue.append(task_id)
            self._sort_queue()

    # ── Status ───────────────────────────────────────────────

    def status(self) -> dict:
        """Trả về tổng quan queue status"""
        return {
            "total": len(self.tasks),
            "pending": sum(1 for t in self.tasks.values() if t["status"] == "pending"),
            "in_progress": sum(1 for t in self.tasks.values() if t["status"] == "in_progress"),
            "completed": len(self.completed),
            "failed": len(self.failed),
            "estimated_total_time": sum(
                t["estimated_time_sec"]
                for t in self.tasks.values()
                if t["status"] in ("pending", "in_progress")
            ),
        }

    def get_tasks_by_scene(self, scene_id: str) -> list:
        """Lấy tất cả tasks cho 1 scene"""
        return [t for t in self.tasks.values() if t["scene_id"] == scene_id]

    # ── Save/Load ────────────────────────────────────────────

    def _save_state(self):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        state = {
            "tasks": self.tasks,
            "queue_order": list(self.queue),
            "completed": self.completed,
            "failed": self.failed,
            "status": self.status(),
        }

        with open(meta_dir / "scheduler_state.json", "w") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

        print(f"  Saved to {meta_dir}/scheduler_state.json")


if __name__ == "__main__":
    scheduler = Scheduler("/home/ngovan960/Documents/remotion_ai_studio")

    test_plan = {
        "total_scenes": 2,
        "total_assets": 4,
        "assets": [
            {"id": "a1", "scene_id": "s1", "type": "image", "priority": 0, "estimated_gen_time_sec": 15},
            {"id": "a2", "scene_id": "s1", "type": "audio", "priority": 1, "estimated_gen_time_sec": 10},
            {"id": "a3", "scene_id": "s2", "type": "animation", "priority": 2, "estimated_gen_time_sec": 25},
            {"id": "a4", "scene_id": "s2", "type": "image", "priority": 2, "estimated_gen_time_sec": 15},
        ],
        "voiceover_segments": [
            {"scene_id": "s1", "estimated_words": 50, "estimated_duration_sec": 20, "priority": 1},
            {"scene_id": "s2", "estimated_words": 30, "estimated_duration_sec": 12, "priority": 2},
        ],
    }

    ids = scheduler.enqueue_plan(test_plan)
    print(f"\nTask IDs: {ids}")
    print(json.dumps(scheduler.status(), indent=2))

    task = scheduler.next_task()
    print(f"\nNext task: {task}")

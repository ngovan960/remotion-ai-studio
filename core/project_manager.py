#!/usr/bin/env python3
"""
Project Manager — Main Orchestrator Agent
Takes topic + duration → returns complete production plan

Pipeline: classify → plan → schedule → quality check → ready for render
"""
import json
import time
from pathlib import Path
from .config import CoreConfig
from .classifier import Classifier
from .planner import Planner
from .scheduler import Scheduler
from .quality import QualityGate


class ProjectManager:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else CoreConfig.default_project_dir()
        self.classifier = Classifier(self.project_dir)
        self.planner = Planner(self.project_dir)
        self.scheduler = Scheduler(self.project_dir)
        self.quality = QualityGate(self.project_dir)

    def create_project(self, topic: str, duration_seconds: int = 60) -> dict:
        """
        Full pipeline: topic + duration → production plan
        Trả về complete project plan nếu quality check passed
        """
        print(f"\n{'='*60}")
        print(f"  REMOTION AI STUDIO — New Project")
        print(f"  Topic: {topic}")
        print(f"  Duration: {duration_seconds}s")
        print(f"{'='*60}")

        start_time = time.time()

        # Step 1: Classify
        classification = self.classifier.classify(topic)

        # Step 2: Plan
        plan = self.planner.plan(classification, duration_seconds)

        # Step 3: Schedule
        task_ids = self.scheduler.enqueue_plan(plan)

        # Step 4: Quality gate
        quality_result = self.quality.validate_plan(plan)

        elapsed = round(time.time() - start_time, 2)

        project = {
            "topic": topic,
            "duration_seconds": duration_seconds,
            "classification": classification,
            "plan": plan,
            "task_ids": task_ids,
            "quality": quality_result,
            "scheduler_status": self.scheduler.status(),
            "elapsed_seconds": elapsed,
            "ready_for_render": quality_result["passed"],
        }

        self._save_project(project)

        print(f"\n{'='*60}")
        print(f"  PROJECT READY: {'✅ PASS' if project['ready_for_render'] else '❌ FAIL'}")
        print(f"  Quality score: {quality_result['score']}")
        print(f"  Tasks: {len(task_ids)}")
        print(f"  Time: {elapsed}s")
        print(f"{'='*60}")

        return project

    # ── Convenience methods ──────────────────────────────────

    def get_next_task(self) -> dict | None:
        """Lấy task tiếp theo từ queue"""
        return self.scheduler.next_task()

    def complete_task(self, task_id: str, result: dict | None = None):
        """Đánh dấu task hoàn thành"""
        self.scheduler.complete_task(task_id, result)

    def fail_task(self, task_id: str, error: str = ""):
        """Đánh dấu task failed"""
        self.scheduler.fail_task(task_id, error)

    def retry_task(self, task_id: str):
        """Retry failed task"""
        self.scheduler.retry_task(task_id)

    def queue_status(self) -> dict:
        """Trạng thái hiện tại của queue"""
        return self.scheduler.status()

    # ── Save ─────────────────────────────────────────────────

    def _save_project(self, project: dict):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        with open(meta_dir / "project.json", "w") as f:
            json.dump(project, f, indent=2, ensure_ascii=False)

        print(f"\n  Saved to {meta_dir}/project.json")


if __name__ == "__main__":
    pm = ProjectManager("/home/ngovan960/Documents/remotion_ai_studio")

    result = pm.create_project(
        topic="The History of Ancient Egypt",
        duration_seconds=120,
    )

    print(f"\nReady for render: {result['ready_for_render']}")
    print(f"Quality score: {result['quality']['score']}")
    print(f"Total tasks: {len(result['task_ids'])}")

    # Demo: process first task
    task = pm.get_next_task()
    if task:
        print(f"\nFirst task: {task['type']} — {task['asset_type']}")
        pm.complete_task(task["id"], {"status": "generated"})
        print(f"Queue status: {pm.queue_status()}")

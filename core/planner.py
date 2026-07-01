#!/usr/bin/env python3
"""
Planner Agent
Tính toán assets cần thiết dựa trên domain + capabilities + duration
"""
import json
from pathlib import Path
from .config import CoreConfig


class Planner:
    def __init__(self, project_dir=None):
        self.project_dir = Path(project_dir) if project_dir else CoreConfig.default_project_dir()
        self.domains = CoreConfig.DOMAINS

    def plan(self, classification: dict, duration_seconds: int) -> dict:
        """
        Tạo production plan từ classification + duration
        Trả về: {scenes, assets, voiceover_segments, total_estimated_time}
        """
        domain = classification["domain"]
        capabilities = classification["capabilities"]

        print(f"\n📋 Planner: Planning {duration_seconds}s video for domain '{domain}'")
        print(f"  Capabilities: {capabilities}")

        domain_config = self.domains.get(domain, self.domains["education"])

        scenes = self._plan_scenes(duration_seconds, domain_config)
        assets = self._plan_assets(scenes, capabilities, domain_config)
        voiceover = self._plan_voiceover(scenes)

        plan = {
            "domain": domain,
            "domain_config": domain_config,
            "duration_seconds": duration_seconds,
            "total_scenes": len(scenes),
            "total_assets": len(assets),
            "scenes": scenes,
            "assets": assets,
            "voiceover_segments": voiceover,
            "estimated_render_time_sec": self._estimate_render_time(scenes, assets),
        }

        self._save_plan(plan)

        print(f"  Scenes: {len(scenes)}")
        print(f"  Assets: {len(assets)}")
        print(f"  Voiceover segments: {len(voiceover)}")
        print(f"  Est. render: {plan['estimated_render_time_sec']}s")

        return plan

    # ── Scene planning ───────────────────────────────────────

    def _plan_scenes(self, duration_sec: int, domain_config: dict) -> list:
        """Chia duration thành scenes"""
        pacing = domain_config.get("pacing", "medium")

        scene_lengths = {
            "slow": 20,
            "slow_build": 15,
            "medium": 12,
            "fast": 8,
        }
        avg_scene_len = scene_lengths.get(pacing, 12)
        num_scenes = max(2, duration_sec // avg_scene_len)

        scenes = []
        remaining = duration_sec
        act_names = ["hook", "setup", "conflict", "climax", "resolution"]

        for i in range(num_scenes):
            act = act_names[min(i, len(act_names) - 1)]
            if i == 0:
                scene_dur = min(8, remaining)
            elif i == num_scenes - 1:
                scene_dur = remaining
            else:
                scene_dur = remaining // (num_scenes - i)

            scene_dur = max(CoreConfig.MIN_SCENE_DURATION_SEC, scene_dur)
            remaining -= scene_dur

            scenes.append({
                "id": f"scene_{i + 1:03d}",
                "number": i + 1,
                "act": act,
                "duration_sec": scene_dur,
                "start_sec": sum(s["duration_sec"] for s in scenes),
            })

            if remaining <= 0:
                break

        return scenes

    # ── Asset planning ───────────────────────────────────────

    def _plan_assets(self, scenes: list, capabilities: list, domain_config: dict) -> list:
        """Tính toán assets cần thiết cho mỗi scene tuân theo công thức phân phối tỷ lệ"""
        assets = []
        asset_id = 0

        N = len(scenes)
        formula = CoreConfig.DEFAULT_COMPOSITION_FORMULA

        # Tính số lượng cảnh cho từng loại hình ảnh/video chính
        num_video = max(1, int(N * formula["video_clip"]))
        num_animation = max(1, int(N * formula["animation"]))
        num_infographic = max(1, int(N * formula["infographic"]))
        num_image = max(1, N - num_video - num_animation - num_infographic)

        # Sắp xếp các cảnh theo độ ưu tiên quan trọng của phân đoạn để phân phối visual asset phù hợp
        # Climax và Hook ưu tiên video_clip, Setup/Conflict ưu tiên animation/image, Resolution ưu tiên infographic/image
        act_priority_map = {
            "climax": 0,
            "hook": 1,
            "conflict": 2,
            "setup": 3,
            "resolution": 4
        }
        scenes_sorted = sorted(scenes, key=lambda s: act_priority_map.get(s["act"], 2))

        scene_visual_mapping = {}
        
        # Phân phối lần lượt các asset theo thứ tự ưu tiên
        video_left = num_video
        animation_left = num_animation
        infographic_left = num_infographic
        image_left = num_image

        for scene in scenes_sorted:
            act = scene["act"]
            if act == "climax" and video_left > 0:
                visual = "video_clip"
                video_left -= 1
            elif act == "hook" and video_left > 0:
                visual = "video_clip"
                video_left -= 1
            elif act == "resolution" and infographic_left > 0:
                visual = "infographic"
                infographic_left -= 1
            elif video_left > 0:
                visual = "video_clip"
                video_left -= 1
            elif animation_left > 0:
                visual = "animation"
                animation_left -= 1
            elif infographic_left > 0:
                visual = "infographic"
                infographic_left -= 1
            else:
                visual = "image"
                image_left -= 1
            scene_visual_mapping[scene["id"]] = visual

        # Sinh các asset chi tiết cho từng scene
        for scene in scenes:
            scene_id = scene["id"]
            act = scene["act"]
            primary_visual = scene_visual_mapping[scene_id]

            scene_assets = []
            
            # Thêm visual asset chính
            if primary_visual == "infographic":
                # Lựa chọn loại infographic phù hợp dựa trên capabilities hoặc mặc định
                if "timeline" in capabilities:
                    scene_assets.append("timeline")
                elif "map" in capabilities:
                    scene_assets.append("map")
                elif "chart" in capabilities:
                    scene_assets.append("chart")
                else:
                    scene_assets.append("timeline")
            else:
                scene_assets.append(primary_visual)

            # Luôn thêm các thành phần phụ trợ (text overlay, voiceover, audio) theo phân cảnh
            if act in ("hook", "resolution"):
                scene_assets.append("text_overlay")
                scene_assets.append("audio")
            else:
                scene_assets.append("voiceover")

            if act == "climax" and "audio" not in scene_assets:
                scene_assets.append("audio")

            # Ghi nhận các asset vào kế hoạch sản xuất
            for asset_type in scene_assets:
                asset_id += 1
                assets.append({
                    "id": f"asset_{asset_id:04d}",
                    "scene_id": scene_id,
                    "type": asset_type,
                    "priority": self._asset_priority(asset_type, act),
                    "estimated_gen_time_sec": self._estimate_gen_time(asset_type),
                })

        return assets

    def _base_assets_for_act(self, act: str, capabilities: list, typical: list) -> list:
        """Assets mặc định cho mỗi act"""
        base = {
            "hook": ["image", "text_overlay", "audio"],
            "setup": ["image", "animation", "voiceover"],
            "conflict": ["image", "animation", "voiceover"],
            "climax": ["image", "video_clip", "voiceover", "audio"],
            "resolution": ["image", "text_overlay", "audio"],
        }

        result = list(base.get(act, ["image", "voiceover"]))

        for cap in capabilities:
            if cap not in result:
                result.append(cap)

        for t in typical:
            if t not in result and t in CoreConfig.ASSET_TYPES:
                result.append(t)

        return result

    def _asset_priority(self, asset_type: str, act: str) -> int:
        if act == "hook":
            return CoreConfig.PRIORITY_CRITICAL
        if asset_type in ("voiceover", "audio"):
            return CoreConfig.PRIORITY_HIGH
        if act == "climax":
            return CoreConfig.PRIORITY_HIGH
        return CoreConfig.PRIORITY_MEDIUM

    def _estimate_gen_time(self, asset_type: str) -> int:
        """Ước tính thời gian tạo asset (seconds)"""
        times = {
            "image": 15,
            "video_clip": 30,
            "audio": 10,
            "voiceover": 20,
            "text_overlay": 5,
            "animation": 25,
            "chart": 10,
            "map": 12,
            "timeline": 12,
            "code_snippet": 8,
            "screen_recording": 45,
        }
        return times.get(asset_type, 15)

    # ── Voiceover planning ───────────────────────────────────

    def _plan_voiceover(self, scenes: list) -> list:
        """Plan voiceover segments"""
        segments = []
        for scene in scenes:
            word_count = int(scene["duration_sec"] * 2.5)
            segments.append({
                "scene_id": scene["id"],
                "estimated_words": word_count,
                "estimated_duration_sec": scene["duration_sec"],
                "priority": CoreConfig.PRIORITY_HIGH if scene["act"] in ("hook", "climax") else CoreConfig.PRIORITY_MEDIUM,
            })
        return segments

    # ── Render time estimation ───────────────────────────────

    def _estimate_render_time(self, scenes: list, assets: list) -> int:
        """Ước tính thời gian render tổng"""
        total_gen = sum(a["estimated_gen_time_sec"] for a in assets)
        render_base = sum(s["duration_sec"] for s in scenes) * 2
        return total_gen + render_base

    # ── Save ─────────────────────────────────────────────────

    def _save_plan(self, plan: dict):
        meta_dir = self.project_dir / "metadata"
        meta_dir.mkdir(parents=True, exist_ok=True)

        with open(meta_dir / "production_plan.json", "w") as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)

        print(f"  Saved to {meta_dir}/production_plan.json")


if __name__ == "__main__":
    planner = Planner("/home/ngovan960/Documents/remotion_ai_studio")

    test_class = {
        "domain": "history",
        "capabilities": ["timeline", "map", "animation"],
        "domain_config": CoreConfig.DOMAINS["history"],
    }

    plan = planner.plan(test_class, duration_seconds=120)
    print(json.dumps(plan, indent=2, ensure_ascii=False)[:500])

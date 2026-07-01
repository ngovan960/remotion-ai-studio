#!/usr/bin/env python3
"""
Core Configuration
Central config for the entire production pipeline
"""
import os
from pathlib import Path


class CoreConfig:
    # ── Domains ──────────────────────────────────────────────
    DOMAINS = {
        "documentary": {
            "name": "Documentary",
            "style": "cinematic",
            "pacing": "slow",
            "tone": "authoritative",
            "typical_assets": ["timeline", "map", "archival", "talking_head"],
        },
        "history": {
            "name": "History",
            "style": "vintage",
            "pacing": "medium",
            "tone": "narrative",
            "typical_assets": ["timeline", "map", "portrait", "artifact"],
        },
        "education": {
            "name": "Education",
            "style": "clean",
            "pacing": "medium",
            "tone": "instructive",
            "typical_assets": ["chart", "diagram", "code", "animation"],
        },
        "horror": {
            "name": "Horror",
            "style": "dark",
            "pacing": "slow_build",
            "tone": "suspenseful",
            "typical_assets": ["jump_scare", "ambient", "vfx", "sound_design"],
        },
        "marketing": {
            "name": "Marketing",
            "style": "bright",
            "pacing": "fast",
            "tone": "persuasive",
            "typical_assets": ["product_shot", "testimonial", "cta", "logo"],
        },
    }

    # ── Capability detection keywords ────────────────────────
    CAPABILITY_KEYWORDS = {
        "timeline": ["history", "evolution", "timeline", "chronological", "years ago", "century"],
        "map": ["location", "country", "world", "geography", "travel", "region"],
        "chart": ["data", "statistics", "numbers", "percentage", "growth", "trend"],
        "code": ["programming", "code", "software", "algorithm", "api", "developer"],
        "screen_recording": ["tutorial", "demo", "walkthrough", "screen", "app", "website"],
        "animation": ["process", "flow", "how it works", "mechanism", "cycle"],
        "talking_head": ["interview", "opinion", "expert", "analysis", "commentary"],
    }

    # ── Asset types ──────────────────────────────────────────
    ASSET_TYPES = [
        "image",
        "video_clip",
        "audio",
        "voiceover",
        "text_overlay",
        "animation",
        "chart",
        "map",
        "timeline",
        "code",
        "code_snippet",
        "screen_recording",
        "talking_head",
    ]

    # ── Priority levels ──────────────────────────────────────
    PRIORITY_CRITICAL = 0
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    # ── Quality thresholds ───────────────────────────────────
    MAX_PROMPT_LENGTH = 500
    MIN_PROMPT_LENGTH = 10
    MAX_SCENE_DURATION_SEC = 60
    MIN_SCENE_DURATION_SEC = 3
    MAX_TOTAL_DURATION_SEC = 1800  # 30 min
    MIN_TOTAL_DURATION_SEC = 15    # 15 sec
    REQUIRED_AUDIO_FORMATS = ("mp3", "wav", "ogg", "aac")

    # ── Paths ────────────────────────────────────────────────
    @staticmethod
    def default_project_dir():
        return Path(os.environ.get(
            "REMOTION_PROJECT_DIR",
            Path(__file__).resolve().parent.parent / "projects"
        ))

    @staticmethod
    def assets_dir(project_dir):
        return Path(project_dir) / "assets"

    @staticmethod
    def metadata_dir(project_dir):
        return Path(project_dir) / "metadata"

    @staticmethod
    def output_dir(project_dir):
        return Path(project_dir) / "output"

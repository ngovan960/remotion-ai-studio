# Production Quality Rules Skill (v2.0)

> 10-point quality validation

## Quality Checklist

```yaml
quality_check:
  1_timing: "Duration = Word Count / 2"
  2_sources: "100% scenes have peer-reviewed source"
  3_image_prompts: "15 elements per prompt"
  4_video_prompts: "5 motion layers per prompt"
  5_consistency: "Character/Environment IDs consistent"
  6_global_style: "Style inherited, not repeated"
  7_asset_budget: "55% image, 15% video, 20% stock, 10% SVG"
  8_shot_planning: "2-4 shots per scene"
  9_visual_rhythm: "No 3 consecutive same camera"
  10_render_strategy: "Video 6s + Freeze 20s Ken Burns"
```

## Validation Scripts

```python
# Timing
def check_timing(scenes):
    for s in scenes:
        expected = len(s["narration"].split()) / 2
        if abs(expected - s["duration"]) > 5:
            return False
    return True

# Prompt completeness
def check_prompts(scenes):
    required = ["subject", "environment", "lighting", "mood", "color"]
    for s in scenes:
        for r in required:
            if r not in s.get("image_prompt", "").lower():
                return False
    return True

# Asset budget
def check_budget(scenes):
    types = [s.get("asset_type") for s in scenes]
    ai_video_pct = types.count("ai_video") / len(types)
    return ai_video_pct <= 0.15  # Max 15% AI video
```

## Minimum Score: 0.90 (9/10)

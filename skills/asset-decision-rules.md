# Asset Decision Rules Skill (v2.0)

> Auto-decision: Khi nào dùng loại asset nào

## Decision Matrix

| Situaction | Asset Type | GPU Cost | Priority |
|------------|------------|----------|----------|
| Text/Overlay | Remotion | Free | 1 |
| Chart/Diagram | SVG | Free | 2 |
| Landscape/Establishing | Stock | Free | 3 |
| Character (static) | AI Image | Low | 4 |
| Character (moving) | AI Video | High | 5 |
| Action scene | AI Video | High | 5 |

## Asset Budget

```yaml
asset_budget:
  remotion: unlimited    # Free
  svg: unlimited         # Free
  stock: 20%             # Free
  ai_image: 55%          # Low GPU
  ai_video: 15%          # High GPU
```

## Auto-Decision Rules

```yaml
auto_decision:
  keywords_to_type:
    timeline: svg
    chart: svg
    map: stock
    landscape: stock
    character_static: ai_image
    character_moving: ai_video
    action: ai_video
    text: remotion
  
  prefer_stock:
    - landscape
    - cityscape
    - nature
    - crowd
```

## Prompt Reuse

```yaml
# Scene 19 reuse scene 1 prompt, change lighting
scene_19:
  reuse: scene_001
  changes:
    - lighting: "warm sunset, golden hour"
    - mood: "reflective, hopeful"
    - camera: "slow pull out"
```

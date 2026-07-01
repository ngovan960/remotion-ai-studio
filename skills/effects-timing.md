# Effects Timing Skill

> Timing chi tiết cho animation, transitions, text overlay

## Effects Template Cho Mỗi Scene

```yaml
scene_effects:
  scene_id: 1
  duration: 33s
  
  ken_burns:
    type: "zoom_in"  # zoom_in|zoom_out|pan_left|pan_right|static
    start_scale: 1.0
    end_scale: 1.15
    duration: 33s
    easing: "ease_in"  # ease_in|ease_out|ease_in_out|linear
  
  transition:
    in_type: "fade_in"
    in_duration: 0.5s
    out_type: "crossfade"
    out_duration: 1.0s
  
  text_overlay:
    - text: "1,000 tỷ tấn"
      appear: 10.0s
      hold: 8.0s
      style: "large, yellow, shadow"
    - text: "Nguồn: Science, 2012"
      appear: 25.0s
      hold: 5.0s
      style: "small, white, bottom"
  
  subtitle:
    enabled: true
    sync: "voiceover"
    style: "bottom, 48px, white"
```

## Ken Burns Types

| Type | Start | End | Duration | Dùng khi |
|------|-------|-----|----------|----------|
| zoom_in | 100% | 115% | 7s | Emphasis |
| zoom_out | 115% | 100% | 7s | Context |
| pan_left | center | left 5% | 7s | Reveal |
| pan_right | center | right 5% | 7s | Reveal |
| static | 100% | 100% | 7s | Text/data |

## Transition Types

| Type | Duration | When |
|------|----------|------|
| cut | 0s | Same action |
| crossfade | 0.5-1s | Scene change |
| dissolve | 1-2s | Time shift |
| fade_to_black | 1-2s | Act ending |
| fade_in | 0.5-1s | Start |

## Text Overlay Timing

```yaml
text_overlay:
  - text: "Key Point"
    appear: 3.5s     # Khi nào hiện
    hold: 5.0s       # Giữ bao lâu
    fade_in: 0.5s    # Fade in duration
    fade_out: 0.5s   # Fade out duration
    position: "center"  # center|top|bottom
    style: "large, white, shadow"
```

## Easing Functions

| Easing | Effect | Dùng khi |
|--------|--------|----------|
| ease_in | Chậm → nhanh | Zoom in |
| ease_out | Nhanh → chậm | Zoom out |
| ease_in_out | Chậm → nhanh → chậm | Smooth |
| linear | Tốc độ đều | Text appear |

## Effects Pipeline

```yaml
# Tạo effects cho TOÀN BỘ video
effects_pipeline:
  - scene: 1
    effects:
      ken_burns: {type: zoom_in, duration: 20s}
      transition: {in: fade_in, out: crossfade}
      text: [{text: "40 tấn", appear: 5s, hold: 10s}]
  
  - scene: 2
    effects:
      ken_burns: {type: pan_right, duration: 28s}
      transition: {in: dissolve, out: cut}
      text: [{text: "66 triệu năm", appear: 3s, hold: 5s}]
```

## Prompt Template

```
Effects for scene [id]:
- Ken Burns: [type], [duration]s
- Transition: [in_type] in, [out_type] out
- Text: [text] at [timing]s for [hold]s
- Subtitle: sync with voiceover
```

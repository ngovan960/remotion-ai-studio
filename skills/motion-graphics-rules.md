# Motion Graphics Rules Skill

> Quy tắc cho animations trong documentary

## Remotion Animation Types

| Type | Mô tả | Dùng khi |
|------|-------|----------|
| **Ken Burns** | Zoom/pan ảnh tĩnh | Tất cả ảnh |
| **Kinetic Typography** | Text moving | Key points |
| **Infographic Build** | Chart/timeline xuất hiện | Data |
| **Map Reveal** | Bản đồ hiện ra | Location |
| **Animated Arrow** | Chỉ dẫn | Flow, direction |
| **Highlight** | Đánh dấu | Emphasis |
| **Particle** | Particles | Abstract, mood |
| **Fade** | Hiện/tan | Transitions |

## Ken Burns Settings

```yaml
ken_burns:
  zoom_in:
    start_scale: 1.0
    end_scale: 1.15
    duration: "scene_duration"
    easing: "ease_in"
  
  zoom_out:
    start_scale: 1.15
    end_scale: 1.0
    duration: "scene_duration"
    easing: "ease_out"
  
  pan_left:
    start_x: "center"
    end_x: "left_5%"
    duration: "scene_duration"
    easing: "linear"
  
  pan_right:
    start_x: "center"
    end_x: "right_5%"
    duration: "scene_duration"
    easing: "linear"
```

## Kinetic Typography

```yaml
kinetic_text:
  text: "66 TRIỆU NĂM"
  position: "center"
  font_size: 72
  color: "#FF0000"
  animation: "fade_in_scale"
  duration: 1.0s
  hold: 3.0s
  fade_out: 0.5s
```

## Infographic Build

```yaml
infographic:
  type: "bar_chart"
  data:
    - label: "Khủng long"
      value: 40
      color: "#e74c3c"
    - label: "Cá sấu"
      value: 1
      color: "#3498db"
  animation: "bars_appear_left_to_right"
  duration: 4.0s
  position: "bottom_right"
```

## Map Reveal

```yaml
map_reveal:
  type: "satellite"
  location: "Yucatan Peninsula, Mexico"
  animation: "zoom_in_from_space"
  duration: 5.0s
  pins:
    - location: "Chicxulub"
      label: "Hố va chạm"
      color: "#e74c3c"
```

## Text Overlay

```yaml
text_overlay:
  text: "Nguồn: Science, 2010"
  position: "bottom_right"
  font_size: 24
  color: "#FFFFFF"
  background: "rgba(0,0,0,0.5)"
  animation: "fade_in"
  duration: 5.0s
```

## Transition Types

| Type | Duration | When |
|------|----------|------|
| fade_in | 0.5s | Scene start |
| fade_out | 0.5s | Scene end |
| crossfade | 1.0s | Scene change |
| dissolve | 1.5s | Time shift |
| cut | 0s | Same action |

## Remotion Code Example

```tsx
// Ken Burns Zoom In
const scale = interpolate(frame, [0, duration], [1, 1.15]);
<div style={{ transform: `scale(${scale})` }}>
  <Img src={image} />
</div>

// Text Fade In
const opacity = interpolate(frame, [0, 30], [0, 1]);
const y = interpolate(frame, [0, 30], [20, 0]);
<div style={{ opacity, transform: `translateY(${y}px)` }}>
  Text
</div>
```

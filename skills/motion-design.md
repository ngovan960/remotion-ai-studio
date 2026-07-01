# Motion Design Skill

> Hiệu ứng chuyển động cho video

## Remotion Effects

| Effect | Mô tả | Dùng khi |
|--------|-------|----------|
| **Fade In** | Hiện từ từ | Scene beginning |
| **Fade Out** | Tan từ từ | Scene ending |
| **Zoom In** | Phóng to | Emphasis |
| **Zoom Out** | Thu nhỏ | Context |
| **Pan Left** | Di chuyển trái | Reveal |
| **Pan Right** | Di chuyển phải | Reveal |
| **Highlight** | Đánh dấu | Key point |
| **Slide In** | Trượt vào | Text appearing |
| **Bounce** | Nảy | Playful content |
| **Rotate** | Xoay | Dynamic content |

## Remotion Code

### Fade In
```tsx
const opacity = interpolate(frame, [0, 30], [0, 1]);
<div style={{ opacity }}>Content</div>
```

### Zoom In
```tsx
const scale = interpolate(frame, [0, 150], [1, 1.1]);
<div style={{ transform: `scale(${scale})` }}>Content</div>
```

### Slide In
```tsx
const x = interpolate(frame, [0, 30], [-100, 0]);
<div style={{ transform: `translateX(${x}%)` }}>Content</div>
```

### Highlight
```tsx
const bgColor = interpolate(frame, [0, 15, 30], ["transparent", "#FFD700", "transparent"]);
<div style={{ backgroundColor: bgColor }}>Key Point</div>
```

## Timing

| Effect | Duration | Easing |
|--------|----------|--------|
| Fade | 0.5-1s | ease_in_out |
| Zoom | 2-5s | ease_in |
| Slide | 0.3-0.5s | ease_out |
| Highlight | 0.5-1s | ease_in_out |

## Prompt Template

```
Motion design: [effect] animation on [content],
[easing] timing, [duration] seconds,
professional, smooth transition
```

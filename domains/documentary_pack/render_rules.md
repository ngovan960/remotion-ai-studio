# Documentary Render Rules

## Render Settings

```yaml
resolution: 1920x1080
fps: 30
codec: h264
bitrate: 8M
audio: aac 192k
```

## Effects

| Effect | When | Settings |
|--------|------|----------|
| **Ken Burns** | Static images | Zoom 100-110%, 5-10s |
| **Crossfade** | Scene transitions | 0.5-1s duration |
| **Fade to Black** | Act endings | 1-2s duration |
| **Text Overlay** | Key points | White, shadow, centered |
| **Subtitle** | Voice-over | Bottom, 48px, white |

## Ken Burns Patterns

| Pattern | Start | End | Duration |
|---------|-------|-----|----------|
| Zoom In | 100% | 110% | 7s |
| Zoom Out | 110% | 100% | 7s |
| Pan Left | Center | Left 5% | 7s |
| Pan Right | Center | Right 5% | 7s |
| Static | 100% | 100% | 7s |

## Transition Rules

| From | To | Transition | Duration |
|------|-----|------------|----------|
| Same scene | Different angle | Cut | 0s |
| Different scene | Same act | Crossfade | 0.5-1s |
| End of act | New act | Fade to Black | 1-2s |
| Time shift | Any | Dissolve | 1-2s |
| Location shift | Any | Crossfade | 0.5-1s |

## FFmpeg Commands

### Ken Burns Zoom In
```bash
ffmpeg -loop 1 -i image.png \
  -vf "scale=8000:-1,zoompan=z='min(zoom+0.0015,1.1)':d=144:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=24" \
  -t 6 -c:v libx264 output.mp4
```

### Crossfade
```bash
ffmpeg -i scene_a.mp4 -i scene_b.mp4 \
  -filter_complex "[0:v][1:v]xfade=transition=fade:duration=1:offset=5" \
  output.mp4
```

### Add Subtitle
```bash
ffmpeg -i video.mp4 -vf "subtitles=subs.srt:force_style='FontSize=24'" output.mp4
```

## Quality Check

- [ ] Resolution 1920x1080?
- [ ] FPS 30?
- [ ] Ken Burns smooth?
- [ ] Transitions clean?
- [ ] Subtitles readable?

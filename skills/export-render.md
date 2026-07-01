# Export & Render Skill

> Settings cho render video

## YouTube Optimal Settings

| Setting | Value | Reason |
|---------|-------|--------|
| Resolution | 1920x1080 | YouTube standard |
| FPS | 30 | Smooth, standard |
| Codec | H.264 | Maximum compatibility |
| Bitrate | 8-12 Mbps | Good quality |
| Audio | AAC 192kbps | YouTube standard |

## Resolution Comparison

| Resolution | Use | File Size |
|------------|-----|-----------|
| 720p | Draft, mobile | Small |
| 1080p | YouTube standard | Medium |
| 1440p | High quality | Large |
| 4K | Premium | Very large |

## FFmpeg Commands

### Basic Render
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -c:a aac output.mp4
```

### YouTube Optimized
```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -preset slow -crf 18 \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  output.mp4
```

### Upscale to 1080p
```bash
ffmpeg -i input.mp4 \
  -vf "scale=1920:1080:flags=lanczos" \
  -c:v libx264 -crf 18 \
  output_1080p.mp4
```

### Add Subtitles
```bash
ffmpeg -i video.mp4 -vf "subtitles=subs.srt:force_style='FontSize=24'" output.mp4
```

## Quality Presets

| Preset | CRF | Speed | Quality |
|--------|-----|-------|---------|
| Draft | 28 | Fast | Low |
| Normal | 23 | Medium | Good |
| High | 18 | Slow | Great |
| Max | 15 | Very slow | Best |

## Export Checklist

- [ ] Resolution matches target?
- [ ] FPS correct?
- [ ] Audio synced?
- [ ] Subtitles burned in?
- [ ] File size reasonable?
- [ ] Playback test passed?

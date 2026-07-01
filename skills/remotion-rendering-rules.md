# Remotion Rendering Rules Skill

> Quy định render, subtitle, overlay, transition

## Render Settings

```yaml
render:
  resolution: "1920x1080"
  fps: 30
  codec: "h264"
  bitrate: "8M"
  audio_codec: "aac"
  audio_bitrate: "192k"
  
  optimization:
    preset: "slow"  # slow = better quality
    crf: 18         # lower = better quality
    tune: "film"    # for documentary
```

## Subtitle Rules

```yaml
subtitle:
  max_chars_per_line: 35
  max_lines: 2
  min_duration: 1.0s
  max_duration: 7.0s
  gap: 0.1s
  position: "bottom"
  font_size: 48
  font_weight: "bold"
  color: "#FFFFFF"
  background: "rgba(0,0,0,0.75)"
  padding: "8px 16px"
  border_radius: 4
  text_shadow: "2px 2px 4px rgba(0,0,0,0.5)"
```

## Subtitle Timing

```yaml
subtitle_timing:
  # Match voiceover segments
  - text: "Năm 1975, một người đàn ông biến mất"
    start: 0.5s
    end: 3.5s
  - text: "Kể từ đêm đó, không ai thấy ông ấy nữa"
    start: 4.0s
    end: 7.0s
```

## Overlay Rules

```yaml
overlay:
  text_overlay:
    position: "center"  # center|top|bottom|top_left|top_right|bottom_left|bottom_right
    font_size: 72
    font_weight: "bold"
    color: "#FFFFFF"
    background: "rgba(0,0,0,0.5)"
    animation: "fade_in_scale"
    duration: 1.0s
    hold: 3.0s
    fade_out: 0.5s
  
  source_overlay:
    position: "bottom_right"
    font_size: 24
    color: "#AAAAAA"
    text: "Nguồn: [citation]"
    animation: "fade_in"
    duration: 5.0s
```

## Safe Areas

```yaml
safe_areas:
  title_safe: 80%    # Text trong 80% center
  action_safe: 90%   # Action trong 90%
  subtitle_zone: "bottom 20%"
  overlay_zone: "top 10%, bottom 10%"
```

## Motion Blur

```yaml
motion_blur:
  enabled: true
  shutter_angle: 180  # Standard cinematic
  samples: 8          # Higher = better quality
```

## Export Formats

```yaml
export:
  youtube:
    resolution: "1920x1080"
    fps: 30
    codec: "h264"
    bitrate: "8M"
  
  archive:
    resolution: "1920x1080"
    fps: 30
    codec: "h264"
    bitrate: "15M"
  
  preview:
    resolution: "1280x720"
    fps: 24
    codec: "h264"
    bitrate: "4M"
```

## Remotion Composition

```tsx
// Main composition structure
<AbsoluteFill>
  {/* Layer 1: Background */}
  <Sequence from={0}>
    <SceneBackground scene={scene} />
  </Sequence>
  
  {/* Layer 2: Ken Burns */}
  <Sequence from={0}>
    <KenBurn effect={scene.ken_burns} />
  </Sequence>
  
  {/* Layer 3: Text Overlay */}
  <Sequence from={scene.textTiming}>
    <TextOverlay text={scene.text} />
  </Sequence>
  
  {/* Layer 4: Subtitle */}
  <Sequence from={0}>
    <Subtitle text={scene.narration} />
  </Sequence>
  
  {/* Layer 5: Source */}
  <Sequence from={scene.sourceTiming}>
    <SourceOverlay text={scene.source} />
  </Sequence>
</AbsoluteFill>
```

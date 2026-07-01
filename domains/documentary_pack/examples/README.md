# Documentary Examples

## Example 1: History Documentary

### Input
```
Topic: "Lịch sử Hà Nội qua các thời kỳ"
Duration: 15 phút
```

### Classification
```yaml
domain: history
capabilities: [timeline, map, portrait]
```

### Asset Plan
```yaml
images: 45 (50%)
stock: 27 (30%)
video_clips: 14 (15%)
charts: 9 (5%)
total: 95
```

### Sample Prompts

```yaml
scene_01:
  subject: "Ancient Hanoi citadel, stone walls, morning mist"
  environment: "11th century Vietnam, imperial palace"
  action: "Guard standing watch"
  camera: "wide_shot"
  lighting: "morning mist, soft diffused"
  style: "cinematic, 35mm grain, historical"
  color: "muted earth tones, sepia accents"

scene_02:
  subject: "French colonial building, ornate architecture"
  environment: "1880s Hanoi, French Quarter"
  action: "Horse carriage passing"
  camera: "medium_shot"
  lighting: "golden hour, warm"
  style: "vintage, sepia, historical"
  color: "warm browns, golden"
```

### Audio Plan
```yaml
music: "epic orchestral, Vietnamese instruments, 110 BPM"
sfx: ["horse carriage", "street vendors", "temple bells"]
voice: "authoritative, measured pace"
```

---

## Example 2: Science Documentary

### Input
```
Topic: "Công nghệ AI trong y tế"
Duration: 12 phút
```

### Classification
```yaml
domain: documentary
capabilities: [chart, diagram]
```

### Asset Plan
```yaml
images: 36 (50%)
stock: 22 (30%)
video_clips: 11 (15%)
charts: 7 (5%)
total: 76
```

### Sample Prompts

```yaml
scene_01:
  subject: "Modern hospital, AI diagnostic screen"
  environment: "2026 hospital, clean, high-tech"
  action: "Doctor reviewing AI analysis"
  camera: "medium_shot"
  lighting: "clinical, bright, clean"
  style: "modern, sleek, technological"
  color: "white, blue accents, clean"

scene_02:
  subject: "AI brain scan analysis, neural network overlay"
  environment: "Medical imaging lab"
  action: "AI processing brain scan"
  camera: "close_up"
  lighting: "blue glow, technological"
  style: "futuristic, medical, clean"
  color: "blue, white, clinical"
```

---

## Example 3: Horror Documentary

### Input
```
Topic: "Những vụ án bí ẩn Việt Nam"
Duration: 20 phút
```

### Classification
```yaml
domain: horror_story
capabilities: []
```

### Asset Plan
```yaml
images: 60 (50%)
stock: 18 (15%)
video_clips: 24 (20%)
sfx: 18 (15%)
total: 120
```

### Sample Prompts

```yaml
scene_01:
  subject: "Abandoned building, overgrown vegetation"
  environment: "Remote Vietnamese village, night"
  action: "Mysterious light in window"
  camera: "wide_shot"
  lighting: "moonlight, eerie blue"
  style: "horror, dark, atmospheric"
  color: "dark blues, shadows, desaturated"

scene_02:
  subject: "Old photograph, faded, damaged"
  environment: "1970s Vietnam, vintage"
  action: "Photo floating in darkness"
  camera: "close_up"
  lighting: "dim, single light source"
  style: "vintage, horror, mysterious"
  color: "sepia, dark, faded"
```

### Audio Plan
```yaml
music: "dark horror ambient, eerie, unsettling, 80 BPM"
sfx: ["door_creak", "wind_howl", "heartbeat", "whisper"]
voice: "measured, suspenseful, pauses for effect"
```

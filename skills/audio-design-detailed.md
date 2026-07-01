# Audio Design Detailed Skill

> Thiết kế audio chi tiết cho MỖI scene

## Audio Template Cho Mỗi Scene

```yaml
scene_audio:
  scene_id: 1
  
  voiceover:
    speed: 120  # words per minute
    tone: "dramatic"
    volume: 0dB
    pause_after: 1s
  
  music:
    mood: "tense"
    tempo: 110
    key: "minor"
    instruments: ["strings", "percussion"]
    volume: -15dB
    fade_in: 2s
    fade_out: 1s
  
  sfx:
    - type: "impact"
      timing: 0.0s
      duration: 2s
      volume: -10dB
    - type: "wind"
      timing: 5.0s
      duration: 10s
      volume: -20dB
  
  silence:
    - timing: 30.0s
      duration: 3s
      reason: "dramatic pause"
```

## Music Mood Map

| Phase | Mood | Tempo | Key | Instruments |
|-------|------|-------|-----|-------------|
| Hook | Tense | 110-120 | Minor | Strings, percussion |
| Setup | Calm | 80-100 | Major | Piano, strings |
| Conflict | Tension | 120-130 | Minor | Strings, brass |
| Climax | Peak | 130-140 | Minor | Full orchestra |
| Resolution | Peaceful | 70-90 | Major | Piano, soft strings |

## SFX Library

| Type | Duration | Use |
|------|----------|-----|
| Impact | 1-2s | Reveal, data point |
| Whoosh | 0.5s | Transition |
| Wind | 5-20s | Nature, atmosphere |
| Thunder | 2-3s | Drama, power |
| Heartbeat | 1-2s | Tension |
| Click | 0.1s | UI interaction |

## Silence Rules

| Type | Duration | When |
|------|----------|------|
| Micro | 0.1-0.3s | Between sentences |
| Dramatic | 1-3s | Before reveal |
| Emphasis | 0.5-1s | After key point |
| Transition | 1-2s | Between sections |

## Audio Mixing

```
Voice:    0dB    ████████████████████
Music:   -15dB   ████████░░░░░░░░░░░░
SFX:     -12dB   █████████░░░░░░░░░░░
Ambient: -20dB   ████░░░░░░░░░░░░░░░░
```

## Prompt Template

```
Audio design for scene [id]:
- Music: [mood], [tempo] BPM, [instruments]
- SFX: [type] at [timing]
- Voice: [speed] wpm, [tone]
- Silence: [duration]s at [timing]
```

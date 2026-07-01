# Audio Direction Skill (v2.0)

> TTS, MusicGen, AudioGen prompts đầy đủ

## TTS Settings

```yaml
tts:
  voice: "M1|M2|M3|F1|F2|F3"
  emotion: "neutral|dramatic|calm|urgent|intense"
  speed: 120  # words per minute
  pitch: "normal|low|high"
  pause_after_sentence: 0.3s
  pause_after_paragraph: 1.0s
  breathing: true
  emphasis: ["keyword1", "keyword2"]
```

## MusicGen Prompt Format

```yaml
music_prompt:
  genre: "documentary|orchestral|ambient|electronic"
  mood: "tense|calm|intense|hopeful|mysterious"
  energy: 0.0-1.0
  instruments: ["piano", "strings", "percussion"]
  texture: "soft|thick|ambient"
  tempo: 80-130
  key: "major|minor"
  loop: true
  ending: "fade|cut"
```

## AudioGen SFX Format

```yaml
sfx:
  - type: "impact|whoosh|wind|thunder|fire|water"
    prompt: "deep impact boom, low frequency"
    timing: 0.0s
    duration: 2s
    mix: "foreground|background"
    reverb: "none|hall|room"
    stereo: "mono|wide"
    intensity: "low|medium|high"
    fade: "0.5s"
```

## Audio Mixing

```
Voice:    0dB    ████████████████████
Music:   -15dB   ████████░░░░░░░░░░░░
SFX:     -12dB   █████████░░░░░░░░░░░
Ambient: -20dB   ████░░░░░░░░░░░░░░░░
```

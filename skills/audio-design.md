# Audio Design Skill

> Thiết kế âm thanh cho video với AudioGen + MusicGen

## Audio Layers

```
Layer 1: Dialogue/Voice    → Primary (0dB)
Layer 2: Music             → Background (-15dB)
Layer 3: SFX               → Effects (-12dB)
Layer 4: Ambience          → Environment (-20dB)
Layer 5: Silence           → Strategic pauses
```

## Audio by Scene Phase

| Phase | Voice | Music | SFX | Ambience |
|-------|-------|-------|-----|----------|
| Hook | Fast, urgent | Tense, building | Stinger | Minimal |
| Setup | Medium, calm | Soft, ambient | Natural | Environment |
| Conflict | Increasing pace | Building tension | Impacts | Tension |
| Climax | Fast, intense | Peak, dramatic | Impacts | Minimal |
| Resolution | Slow, reflective | Resolving, peaceful | Soft | Natural |

---

## MusicGen (Nhạc nền)

### Model
- **Facebook MusicGen Large** (~4.2 GB)
- VRAM: 4-8 GB
- Chạy local, miễn phí

### Prompt Templates

| Mood | Prompt |
|------|--------|
| Epic | `epic orchestral music, dramatic, cinematic, 120 BPM` |
| Calm | `calm ambient music, piano, peaceful, 70 BPM` |
| Tension | `tense suspenseful music, strings, building, 100 BPM` |
| Mystery | `mysterious ambient, dark pads, atmospheric, 80 BPM` |
| Happy | `upbeat happy music, major key, energetic, 120 BPM` |
| Sad | `sad emotional music, piano, cello, minor key, 70 BPM` |
| Tech | `futuristic electronic, synth, clean, 110 BPM` |
| Horror | `dark horror ambient, eerie, unsettling, 80 BPM` |

### Code Example

```python
from audiocraft.models import MusicGen

model = MusicGen.get_pretrained('facebook/musicgen-large')
model.set_generation_params(duration=30)

# Generate music
wav = model.generate(["epic orchestral music, dramatic, cinematic"])

# Save
import soundfile as sf
sf.write('music.mp3', wav[0].cpu().numpy(), 32000)
```

### Music Timing

| Video Duration | Music Duration | Loop? |
|----------------|----------------|-------|
| < 30s | Match video | No |
| 30s - 2min | Match video | No |
| 2min - 5min | Loop hoặc extend | Yes |
| > 5min | Loop với fade | Yes |

---

## AudioGen (SFX)

### Model
- **Facebook AudioGen Medium** (~3.4 GB)
- VRAM: 2-4 GB
- Chạy local, miễn phí

### SFX Categories & Prompts

#### Transition Sounds
| Type | Prompt |
|------|--------|
| Whoosh | `whoosh transition sound effect, fast movement` |
| Swipe | `swipe transition, digital, clean` |
| Fade | `soft fade transition, gentle` |
| Glitch | `digital glitch transition, tech` |

#### Impact Sounds
| Type | Prompt |
|------|--------|
| Boom | `deep boom impact, cinematic, low frequency` |
| Hit | `sharp hit impact, punch, aggressive` |
| Crash | `glass crash, breaking, dramatic` |
| Slam | `heavy slam, door closing, forceful` |

#### Nature Sounds
| Type | Prompt |
|------|--------|
| Wind | `wind blowing, outdoor, natural` |
| Rain | `rain falling, gentle, ambient` |
| Birds | `birds chirping, morning, peaceful` |
| Thunder | `distant thunder, rumbling, dramatic` |
| Ocean | `ocean waves, gentle, beach` |

#### Urban Sounds
| Type | Prompt |
|------|--------|
| Traffic | `city traffic, cars passing, urban` |
| Footsteps | `footsteps on pavement, walking` |
| Crowd | `crowd talking, background chatter` |
| Siren | `distant siren, emergency` |

#### Tech Sounds
| Type | Prompt |
|------|--------|
| Beep | `digital beep, notification, clean` |
| Scan | `scanning sound, futuristic, tech` |
| Data | `data processing, computing, digital` |
| Interface | `UI click, button press, interface` |

#### Ambience
| Type | Prompt |
|------|--------|
| Lab | `laboratory ambient, humming equipment, quiet` |
| Office | `office ambient, keyboard typing, quiet chatter` |
| City | `city ambient, distant traffic, urban atmosphere` |
| Forest | `forest ambient, birds, wind in trees` |
| Space | `space ambient, deep, atmospheric, ethereal` |

### Code Example

```python
from audiocraft.models import AudioGen

model = AudioGen.get_pretrained('facebook/audiogen-medium')
model.set_generation_params(duration=3)

# Generate SFX
wav = model.generate(["whoosh transition sound effect"])

# Save
import soundfile as sf
sf.write('sfx.mp3', wav[0].cpu().numpy(), 32000)
```

---

## SFX Timing với Script

### Mapping Script → SFX

```
Script Segment              → SFX Type
─────────────────────────────────────────
"Everything changed"        → Boom impact
Scene transition            → Whoosh
Data appearing              → Digital scan
Dramatic pause              → Silence + subtle drone
Reveal moment               → Impact + reverb
Tension building            → Rising tone
Resolution                  → Soft fade
```

### SFX Placement Rules

| Rule | Description |
|------|-------------|
| On beat | SFX at scene transitions |
| On action | SFX match visual action |
| Not overlap | SFX shouldn't overlap voice |
| Subtle | SFX should support, not dominate |

### Timing Example (10-min video)

```
0:00 - Hook           → Stinger SFX
0:30 - Scene change   → Whoosh
1:00 - Data appear    → Digital scan
2:00 - Tension build  → Rising tone
3:00 - Reveal         → Impact + reverb
4:00 - Scene change   → Whoosh
5:00 - Midpoint       → Dramatic boom
6:00 - Escalation     → Rising tension
7:00 - Climax         → Peak impact
8:00 - Resolution     → Soft fade
9:00 - End            → Final note
```

---

## Audio Mixing Levels

```
Voice:    0 dB    ████████████████████ (Primary)
Music:   -15 dB   ████████░░░░░░░░░░░░ (Background)
SFX:     -12 dB   █████████░░░░░░░░░░░ (Effects)
Ambient: -20 dB   ████░░░░░░░░░░░░░░░░ (Background)
```

## Silence Design

| Type | Duration | Use |
|------|----------|-----|
| Micro pause | 0.1-0.3s | Between sentences |
| Dramatic pause | 1-2s | Before reveal |
| Emphasis pause | 0.5-1s | After key point |
| Transition | 1-3s | Between sections |

---

## Workflow: Audio Generation

```
1. Script Analysis
   └── Identify SFX points in script
   
2. Music Generation (MusicGen)
   ├── Create background track
   ├── Duration = video duration
   └── Mood matches scene phases
   
3. SFX Generation (AudioGen)
   ├── Generate each SFX individually
   ├── Duration: 2-5 seconds each
   └── Match script timing
   
4. Voice Generation (Fish Speech)
   └── Generate narration
   
5. Audio Mixing
   ├── Layer 1: Voice (0dB)
   ├── Layer 2: Music (-15dB)
   ├── Layer 3: SFX (-12dB)
   └── Layer 4: Ambient (-20dB)
   
6. Export
   └── Final audio mix
```

---

## Quality Check

- [ ] Music mood matches scene?
- [ ] SFX timing aligns with script?
- [ ] No SFX overlapping voice?
- [ ] Music volume appropriate?
- [ ] Ambient not distracting?
- [ ] Silence used for emphasis?

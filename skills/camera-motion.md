# Camera Motion Skill

> Phong tr.camera cho video AI

## Motion Types

| Motion | Description | Effect | Prompt Keyword |
|--------|-------------|--------|----------------|
| **Static** | Không chuyển động | Stability, calm | `static camera` |
| **Pan** | Quay ngang | Reveal, follow | `slow pan left/right` |
| **Tilt** | Quay dọc | Scale, power | `tilt up/down` |
| **Truck** | Di chuyển ngang | Tracking | `truck left/right` |
| **Dolly** | Di chuyển tới lui | Intimacy, focus | `dolly in/out` |
| **Zoom** | Thu phóng | Emphasis | `slow zoom in` |
| **Orbit** | Quay quanh | 360° view | `orbit around subject` |
| **Crane** | Di chuyển lên xuống | Epic, scale | `crane shot up` |
| **Handheld** | Run tay | Realism, tension | `handheld camera` |
| **Steadicam** | Mượt mà | Professional | `steadicam follow` |
| **FPV** | Góc nhìn thứ nhất | Immersive | `FPV drone shot` |

## Motion Speed

| Speed | Duration (10m) | Feel |
|-------|----------------|------|
| Very Slow | 20-30s per move | Meditative |
| Slow | 10-15s per move | Calm, deliberate |
| Medium | 5-8s per move | Natural |
| Fast | 2-3s per move | Energetic |
| Very Fast | <1s per move | Action, chaos |

## Motion Combos

| Combo | Effect | Example |
|-------|--------|---------|
| Dolly + Zoom | Vertigo effect | Dramatic reveal |
| Pan + Tilt | Reveal | Landscape |
| Track + Follow | Documentary | Character journey |
| Crane up + Wide | Epic opening | Establishing shot |

## Prompt Template

```
[Speed] [Motion type] shot, [subject], [environment],
cinematic movement, [duration]
```

Examples:
- `Slow dolly in on scientist, laboratory, cinematic`
- `Drone shot orbiting around building, aerial view, epic`
- `Handheld camera following person through crowd, documentary style`

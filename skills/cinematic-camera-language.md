# Cinematic Camera Language Skill (v2.0)

> Quy chuẩn camera với đầy đủ thông số

## Camera Settings

```yaml
camera:
  type: "drone|wide|medium|close|macro|static|tracking|handheld"
  lens: "16mm|24mm|35mm|50mm|85mm|100mm"
  height: "eye_level|low_angle|high_angle|bird_eye|worm_eye"
  angle: "0-90 degrees"
  movement: "static|push_in|pull_out|pan_left|pan_right|orbit|tracking|crane|handheld"
  dof: "deep|moderate|shallow|very_shallow"
  parallax: true|false
  focus: "subject|background|rack"
```

## Camera by Scene Type

| Scene Type | Camera | Lens | Height | Movement |
|------------|--------|------|--------|----------|
| Hook | drone | 24mm | low angle | push in |
| Establishing | wide | 24mm | eye level | pan |
| Detail | close | 85mm | eye level | static |
| Action | tracking | 35mm | low angle | tracking |
| Data | static | flat | straight | static |
| Conclusion | drone | 24mm | bird eye | pull out |

## Visual Rhythm

```
Scene 1: Wide (establishing)
Scene 2: Medium (action)
Scene 3: Close-up (detail)
Scene 4: Macro (texture)
Scene 5: Drone (scale)
Scene 6: Diagram (data)
Scene 7: Map (location)
Scene 8: Stock (real)
```

**Rule:** Không 3 scene liên tiếp cùng camera type

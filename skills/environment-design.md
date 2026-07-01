# Environment Design Skill

> Thiết kế bối cảnh cho video

## Environment Types

| Type | Elements | Mood | Lighting |
|------|----------|------|----------|
| **Office** | Desk, computer, window | Professional | Natural/fluorescent |
| **Laboratory** | Equipment, screens, glass | Scientific | Blue neon |
| **Nature** | Trees, sky, water | Peaceful | Natural light |
| **Urban** | Buildings, traffic, lights | Energetic | Mixed |
| **Home** | Furniture, warm colors | Intimate | Warm, soft |
| **Industrial** | Machines, pipes, metal | Gritty | Harsh, contrast |
| **Futuristic** | Holograms, neon, sleek | Advanced | Blue, neon |

## Environment Continuity Rules

```
Rule 1: Don't change without transition
  Lab → Lab ✅
  Lab → Desert ❌ (need transition)

Rule 2: Time changes need reason
  Day → Night ❌ (sudden)
  Day → Sunset → Night ✅ (gradual)

Rule 3: Keep props consistent
  Scene 1: Laptop on desk
  Scene 2: Same laptop on desk ✅
  Scene 3: Different laptop ❌
```

## Environment Prompt Template

```
[Environment type], [time of day], [weather], [lighting],
[key objects], [mood], [color palette]
```

Examples:
- `Modern laboratory, night, blue neon lighting, server racks, mysterious, blue tones`
- `Forest clearing, morning, foggy, natural light, ancient trees, peaceful, green tones`
- `City rooftop, sunset, clear sky, golden hour, urban skyline, hopeful, warm tones`

## Color Script for Environments

```markdown
| Time Range | Environment | Color Palette | Lighting |
|------------|-------------|---------------|----------|
| 0-2min | Lab | Blue, cool | Neon |
| 2-5min | Office | Neutral, warm | Natural |
| 5-8min | Outdoor | Green, earth | Sunset |
| 8-10min | Lab (return) | Blue, calm | Dim |
```

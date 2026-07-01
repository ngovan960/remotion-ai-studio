# Transition Skill

> Hiệu ứng chuyển cảnh cho video

## Transition Types

| Type | Duration | When | Effect |
|------|----------|------|--------|
| **Cut** | 0s | Same action | Instant change |
| **Crossfade** | 0.5-1s | Scene change | Smooth blend |
| **Fade to Black** | 1-2s | Act ending | Dramatic pause |
| **Fade from Black** | 1s | Act beginning | New section |
| **Slide Left** | 0.5s | Next topic | Directional |
| **Slide Right** | 0.5s | Previous topic | Directional |
| **Zoom In** | 0.5s | Emphasis | Focus |
| **Zoom Out** | 0.5s | Reveal | Context |
| **Dissolve** | 1-2s | Time passing | Dreamy |
| **Wipe** | 0.5s | Quick change | Energetic |

## Transition Rules

| Situation | Use |
|-----------|-----|
| Same scene, different angle | Cut |
| Different scene, same act | Crossfade |
| End of act | Fade to Black |
| Start of act | Fade from Black |
| Time passing | Dissolve |
| Flashback | Dissolve + color shift |
| Dream sequence | Dissolve + blur |

## Transition Timing

```
Scene A (end) ──[Transition]── Scene B (start)
                 0.5-1s
                 
Rule: Transition duration = 5-10% of scene duration
Example: 10s scene → 0.5-1s transition
```

## Transition Prompt

```
Crossfade transition between [scene A] and [scene B],
smooth blend, [duration] seconds
```

## Anti-patterns

| ❌ Don't | ✅ Do |
|---------|-------|
| Same transition repeatedly | Vary transitions |
| Transition every cut | Use cuts for same action |
| Long transitions (>2s) | Keep under 1s |
| flashy transitions | Match content mood |

## Quality Check

- [ ] Transitions varied?
- [ ] Duration appropriate?
- [ ] Matches mood?
- [ ] No jarring cuts?

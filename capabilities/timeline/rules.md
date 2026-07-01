# Timeline Visualization Rules

## Layout Types

| Type | Best For | Orientation | Example |
|------|----------|-------------|---------|
| **Linear** | Simple sequences | Horizontal | 2020 → 2021 → 2022 |
| **Vertical** | Long lists | Vertical | Top to bottom |
| **Radial** | Cyclic events | Circular | Seasons, daily routine |
| **Branching** | Forking paths | Tree | Cause → effect chains |
| **Gantt** | Parallel tracks | Horizontal bars | Project phases |

## Spacing Rules

| Element | Minimum | Recommended | Max |
|---------|---------|-------------|-----|
| Event nodes | 40px | 80px | 120px |
| Connector lines | 20px | 40px | 60px |
| Label margin | 8px | 16px | 24px |
| Timeline height | 200px | 300px | 400px |

## Node Styles

| Node Type | Shape | Use Case |
|-----------|-------|----------|
| Milestone | Circle (filled) | Major events |
| Checkpoint | Diamond | Intermediary points |
| Event | Rounded rectangle | Regular events |
| Current | Glowing circle | Present moment |

## Animation Rules

| Animation | Duration | Use Case |
|-----------|----------|----------|
| Sequential reveal | 0.5s per node | Story progression |
| Fade in | 0.3s | Individual events |
| Line draw | 0.4s | Connection reveal |
| Scale bounce | 0.2s | Milestone emphasis |

## Color Coding

| Category | Primary | Secondary |
|----------|---------|-----------|
| Past | Gray (#666) | Light gray (#999) |
| Present | Blue (#2196F3) | Light blue (#BBDEFB) |
| Future | Green (#4CAF50) | Light green (#C8E6C9) |
| Critical | Red (#F44336) | Light red (#FFCDD2) |
| Milestone | Gold (#FFD700) | Light gold (#FFF9C4) |

## Prompt Template

```
Timeline visualization: [event count] events,
[time span], [style] style,
[animation] reveal, [color] scheme,
[resolution]
```

## Integration with Domains

### History Videos
- Use linear horizontal layout
- Sepia/muted color palette
- Vintage typography
- Include era labels

### Project Management
- Gantt-style with parallel tracks
- Color by team/status
- Progress indicators
- Milestone highlights

### Biography
- Vertical layout for life events
- Photo integration at milestones
- Age labels
- Achievement highlights

## Quality Checklist

- [ ] Events spaced evenly
- [ ] Labels readable at all zoom levels
- [ ] Color contrast meets WCAG AA
- [ ] Animation smooth (60fps target)
- [ ] Responsive to screen size

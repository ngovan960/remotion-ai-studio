# Map Visualization Rules

## Map Styles

| Style | Use Case | Color Palette |
|-------|----------|---------------|
| **Satellite** | Real-world geography | Natural colors |
| **Terrain** | Physical geography | Earth tones |
| **Street** | Urban navigation | Light gray base |
| **Dark** | Data overlays | Dark gray/black base |
| **Minimal** | Clean data viz | White base |
| **Vintage** | Historical routes | Sepia tones |

## Marker Types

| Marker | Shape | Use Case |
|--------|-------|----------|
| Pin | Teardrop | Single location |
| Cluster | Circle with count | Multiple nearby points |
| Heatmap | Gradient circle | Density visualization |
| Custom | SVG icon | Branding/specific objects |

## Route Styles

| Style | Use Case | Width |
|-------|----------|-------|
| Solid line | Primary route | 3-4px |
| Dashed line | Secondary/alternative | 2px |
| Animated dots | Active movement | 2px |
| Gradient | Progress indication | 3px |

## Zoom Levels

| Level | View | Use Case |
|-------|------|----------|
| 1-3 | Continental | Region overview |
| 4-6 | Country | National context |
| 7-9 | City | Urban detail |
| 10-12 | Street | Local navigation |
| 13+ | Building | Precise location |

## Animation Rules

| Animation | Duration | Use Case |
|-----------|----------|----------|
| Marker appear | 0.3s | Point reveal |
| Route draw | 1-2s | Path animation |
| Zoom transition | 0.8s | Level change |
| Pan | 0.5s/100px | Navigation |
| Pulse | 1s loop | Active location |

## Data Layer Rules

| Layer | Opacity | When |
|-------|---------|------|
| Base map | 100% | Always |
| Route overlay | 90% | Route shown |
| Heatmap | 70% | Density data |
| Markers | 100% | Points shown |
| Labels | 80% | Detail views |

## Prompt Template

```
[Style] map visualization of [region]:
- Points of interest: [POI list]
- Route: [start] to [end]
- Data overlay: [type]
- Camera: [movement]
- Resolution: [quality]
```

## Integration with Domains

### Travel Videos
- Use terrain/satellite style
- Animated route following
- Photo markers at destinations
- Distance/time labels

### Logistics/Shipping
- Dark base map
- Real-time animated routes
- Status color coding
- ETA displays

### Historical Routes
- Vintage map style
- Period-appropriate markers
- Date annotations
- Terrain emphasis

### Weather Maps
- Satellite base
- Animated weather patterns
- Temperature overlays
- Forecast markers

## Quality Checklist

- [ ] Map tiles loaded before animation
- [ ] Markers readable at target zoom
- [ ] Routes clearly visible
- [ ] Labels don't overlap markers
- [ ] Smooth 60fps animations
- [ ] Responsive to aspect ratio

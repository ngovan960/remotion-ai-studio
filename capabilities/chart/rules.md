# Chart Visualization Rules

## Chart Types

| Type | Best For | Data |
|------|----------|------|
| **Bar** | Comparisons | Categories |
| **Line** | Trends over time | Time series |
| **Pie** | Proportions | Parts of whole |
| **Scatter** | Correlations | Two variables |
| **Area** | Cumulative data | Time + volume |
| **Radar** | Multi-factor comparison | Multiple axes |
| **Gauge** | Single metric | KPI |
| **Sankey** | Flow/transfer | Source → target |

## Layout Rules

| Element | Size | Position |
|---------|------|----------|
| Chart area | 70% of canvas | Center |
| Title | 24-32px | Top center |
| Legend | 14-16px | Right or bottom |
| Axis labels | 12-14px | Axes |
| Data labels | 10-12px | On data points |

## Color Palettes

### Categorical (≤8 categories)
```
#2196F3 (blue)    #F44336 (red)     #4CAF50 (green)
#FF9800 (orange)  #9C27B0 (purple)  #00BCD4 (cyan)
#795548 (brown)   #607D8B (gray)
```

### Sequential (data magnitude)
```
Light: #E3F2FD → #90CAF9 → #42A5F5 → #1E88E5 → #1565C0
```

### Diverging (positive/negative)
```
Negative: #F44336 → #EF9A9A
Neutral: #FFFFFF
Positive: #A5D6A7 → #4CAF50
```

## Animation Rules

| Animation | Duration | Use Case |
|-----------|----------|----------|
| Bar grow | 0.5s | Bar chart reveal |
| Line draw | 1s | Trend animation |
| Pie slice | 0.3s per slice | Proportion reveal |
| Data point pop | 0.2s | Point emphasis |
| Label fade | 0.2s | Text appear |

## Axis Rules

| Axis | Style | Gridlines |
|------|-------|-----------|
| X (category) | Solid line, labels below | Light gray dashed |
| Y (value) | Solid line, labels left | Light gray solid |
| Secondary Y | Dashed line, labels right | None |

## Data Label Rules

| Condition | Action |
|-----------|--------|
| >5 categories | Hide individual labels, show on hover |
| <5 categories | Show labels on data points |
| Pie chart | Always show percentage |
| Large values | Use K/M suffix (1000 → 1K) |

## Prompt Template

```
Animated [chart type] showing [data description]:
- [X-axis]: [label]
- [Y-axis]: [label]
- Key insight: [insight]
- Animation: [reveal type]
- Style: [minimal/professional/colorful]
```

## Integration with Domains

### Finance
- Line charts for stock prices
- Candlestick for trading
- Green/red for gains/losses
- Real-time feel animations

### Statistics
- Scatter plots with trend lines
- Confidence intervals
- Error bars
- Distribution curves

### Business Reports
- Bar charts for comparisons
- Pie for market share
- Dashboard layout
- Professional color scheme

### Education
- Simple, clear charts
- Larger labels
- Step-by-step build
- Annotation callouts

## Quality Checklist

- [ ] Data accurately represented
- [ ] Axes properly labeled
- [ ] Legend clear
- [ ] Colors colorblind-safe
- [ ] Readable at target resolution
- [ ] Animations don't distort data

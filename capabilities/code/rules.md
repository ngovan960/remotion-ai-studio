# Code Visualization Rules

## Themes

| Theme | Background | Text | Best For |
|-------|------------|------|----------|
| **Dark+** | #1E1E1E | #D4D4D4 | General coding |
| **Monokai** | #272822 | #F8F8F2 | Creative/modern |
| **Solarized Dark** | #002B36 | #839496 | Eye comfort |
| **One Dark** | #282C34 | #ABB2BF | Modern editors |
| **GitHub Light** | #FFFFFF | #24292E | Documentation |
| **Nord** | #2E3440 | #D8DEE9 | Calm aesthetic |

## Syntax Colors

| Element | Dark Theme | Light Theme |
|---------|------------|-------------|
| Keywords | #C586C0 (purple) | #D73A49 (red) |
| Strings | #CE9178 (orange) | #032F62 (blue) |
| Numbers | #B5CEA8 (green) | #005CC5 (blue) |
| Comments | #6A9955 (green) | #6A737D (gray) |
| Functions | #DCDCAA (yellow) | #6F42C1 (purple) |
| Variables | #9CDCFE (light blue) | #005CC5 (blue) |
| Types | #4EC9B0 (teal) | #005CC5 (blue) |
| Operators | #D4D4D4 (white) | #D73A49 (red) |

## Layout Rules

| Element | Size | Position |
|---------|------|----------|
| Code block | 80% width | Center |
| Line numbers | 12px | Left gutter |
| Font size | 16-20px | In code |
| Padding | 20-30px | Around code |
| Border radius | 8px | Corners |

## Highlight Rules

| Highlight | Style | Use Case |
|-----------|-------|----------|
| Current line | Background alpha 0.1 | Focus |
| Selected lines | Background alpha 0.2 | Emphasis |
| Changed lines | Left border green | Diff |
| Error line | Left border red | Debugging |
| Keyword | Color change | Teaching |

## Animation Rules

| Animation | Duration | Use Case |
|-----------|----------|----------|
| Typewriter | 30ms per char | Code writing |
| Line reveal | 0.1s per line | Block reveal |
| Highlight pulse | 0.5s | Emphasis |
| Fade in | 0.3s | Code appear |
| Scroll | 0.5s/5 lines | Navigation |

## Font Stack

```
Primary:    'JetBrains Mono', 'Fira Code', 'Source Code Pro'
Fallback:   'Consolas', 'Monaco', 'Courier New'
Ligatures:  Enabled (->, !=, ===)
```

## Prompt Template

```
[Language] code visualization:
```
[actual code snippet]
```
- Highlight lines: [line numbers]
- Annotations: [explanations]
- Theme: [theme name]
- Animation: [reveal type]
```

## Integration with Domains

### Programming Tutorials
- Typewriter animation
- Line-by-line explanation
- Error highlighting
- Before/after comparisons

### Tech Explainers
- Code blocks with voiceover
- Key concepts highlighted
- Output shown alongside
- Diagram of code flow

### Code Reviews
- Diff visualization
- Before/after split
- Comment annotations
- Approval indicators

### Algorithm Visualization
- Step-by-step execution
- Variable state display
- Memory visualization
- Time complexity note

## Quality Checklist

- [ ] Syntax correctly highlighted
- [ ] Line numbers aligned
- [ ] Readable at target resolution
- [ ] No horizontal scroll (wrap or ellipsis)
- [ ] Theme consistent throughout
- [ ] Annotations don't obscure code

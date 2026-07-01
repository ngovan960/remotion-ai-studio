# Subtitle Skill (Nâng Cấp)

> Chia subtitle dễ đọc, đúng timing

## Subtitle Rules

| Rule | Value | Reason |
|------|-------|--------|
| Lines per subtitle | 2 | Dễ đọc |
| Characters per line | 35 | Đọc trên mobile |
| Duration min | 1s | Đủ đọc |
| Duration max | 7s | Không quá dài |
| Gap between | 0.1s | Rõ ràng |

## Timing With Voice-over

```yaml
subtitle_timing:
  # Match với voice-over segments
  - text: "Năm 1975, một người đàn ông biến mất"
    start: 0.5s
    end: 3.5s
    words: 9
    wpm: 180
  
  # Pause sau câu
  - text: ""
    start: 3.5s
    end: 4.0s
    type: pause
  
  # Câu tiếp theo
  - text: "Kể từ đêm đó, không ai thấy ông ấy nữa"
    start: 4.0s
    end: 7.0s
    words: 10
    wpm: 170
```

## Highlight Rules

| Highlight | When | Color |
|-----------|------|-------|
| Keyword | Important word | Yellow |
| Name | Character name | Cyan |
| Number | Statistics | Green |
| Emphasis | Strong emotion | Red |

## Subtitle Style

```css
font-size: 48px;
font-weight: bold;
color: white;
background: rgba(0, 0, 0, 0.75);
padding: 8px 16px;
border-radius: 4px;
text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
```

## Prompt Template

```
Subtitle generation: match voice-over timing,
2 lines max, 35 chars per line,
highlight keywords in yellow
```

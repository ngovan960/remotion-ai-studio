# Diagram Thinking Skill

> AI biết khi nào cần diagram và loại nào phù hợp

## Khi Nào Dùng Diagram

| Situaction | Diagram Type |
|------------|--------------|
| Quy trình, bước | Flowchart |
| Cấu trúc hệ thống | Architecture |
| Thời gian, sequence | Timeline |
| Mối quan hệ dữ liệu | ERD |
| Ý tưởng, phân nhánh | Mindmap |
| So sánh | Comparison Table |
| Thống kê | Chart (Bar/Pie/Line) |

## Diagram Types

### Flowchart
```
Dùng khi: Quy trình, decision tree
Ví dụ: Quy trình sản xuất video

[Bắt đầu] → [Phân loại] → [Lập kế hoạch] → [Tạo assets] → [Kết thúc]
```

### Architecture Diagram
```
Dùng khi: Cấu trúc hệ thống
Ví dụ: Cấu trúc Remotion AI Studio

[Core Engine] → [Domain Packs] → [Capability Packs]
      ↓               ↓                ↓
[Classifier]    [Documentary]    [Timeline]
[Planner]       [History]        [Chart]
```

### Timeline
```
Dùng khi: Sự kiện theo thời gian
Ví dụ: Lịch sử AI

1950 → 1980 → 2010 → 2020 → 2026
Turing   ML    Deep    GPT    AI
         Learning        Era
```

### ERD (Entity Relationship)
```
Dùng khi: Mối quan hệ dữ liệu
Ví dụ: Cấu trúc database

[User] 1---N [Video]
[Video] 1---N [Scene]
[Scene] N---1 [Asset]
```

### Mindmap
```
Dùng khi: Phân nhánh ý tưởng
Ví dụ: Các loại video AI

         [Video AI]
        /    |     \
   [Doc]  [Edu]  [Story]
   / | \    | \     | \
 [T] [M] [C] [S] [D] [P]
```

## Prompt Template

```
Create a [diagram_type] showing [topic],
clear labels, clean design, professional style
```

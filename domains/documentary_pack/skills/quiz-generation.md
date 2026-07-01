# Quiz Generation Skill

> Tạo câu hỏi trắc nghiệm cho video giáo dục

## Quiz Types

| Type | Mô tả | Dùng khi |
|------|-------|----------|
| **Multiple Choice** | Chọn 1 từ 4 | Kiến thức cơ bản |
| **True/False** | Đúng/Sai | Kiểm tra hiểu biết |
| **Fill in Blank** | Điền từ | Thuật ngữ |
| **Matching** | Ghép đôi | Định nghĩa |
| **Ordering** | Sắp xếp | Quy trình |

## Cấu Trúc Câu Hỏi

```markdown
## Câu [số]

**Câu hỏi:** [Nội dung]

**A.** [Đáp án A]
**B.** [Đáp án B]
**C.** [Đáp án C]
**D.** [Đáp án D]

**Đáp án:** [Đáp án đúng]

**Giải thích:** [Tại sao đáp án đúng]
```

## Quiz Timing

| Video Length | Số câu hỏi | Vị trí |
|--------------|------------|--------|
| 5 phút | 2-3 câu | Sau mỗi section |
| 10 phút | 4-5 câu | Mỗi 2 phút |
| 20 phút | 8-10 câu | Mỗi 2 phút |

## Quiz Placement

```
Video Flow:
Hook → Content → [QUIZ 1] → Content → [QUIZ 2] → Content → [QUIZ 3] → Summary
```

## Prompt Template

```
Generate [number] quiz questions about [topic],
mix of multiple choice and true/false,
include explanations for each answer,
difficulty: [easy/medium/hard]
```

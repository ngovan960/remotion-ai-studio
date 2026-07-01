# Prompt Awareness Skill (Nâng Cấp)

> Mỗi scene PHẢI có đủ thông tin cho pipeline render tự động

## 8 Elements Required

| Element | Question | Example |
|---------|----------|---------|
| **Subject** | Có ai? | "Female historian, 35yo, glasses" |
| **Environment** | Ở đâu? | "Ancient library, warm light" |
| **Action** | Làm gì? | "Reading manuscript" |
| **Camera** | Góc máy? | "Medium shot, slight low angle" |
| **Lighting** | Ánh sáng? | "Warm golden hour" |
| **Color** | Màu sắc? | "Sepia tones, warm browns" |
| **Style** | Phong cách? | "Cinematic, 35mm grain" |
| **Motion** | Chuyển động? | "Slow dolly forward" |

## Production-Ready Scene Format

```
### SCENE XX
**Goal:** [Mục tiêu truyền đạt]
**Key Message:** [Ý chính duy nhất]
**Duration:** XXs
**Word Count:** XX từ

| Field | Value |
|-------|-------|
| **Narration** | "[text đầy đủ]" |
| **Visual Objective** | [Mục tiêu hình ảnh] |
| **Primary Asset** | [Asset chính] |
| **Secondary Asset** | [Asset phụ] |
| **Camera Motion** | [Chuyển động] |
| **Animation** | [Hiệu ứng] |
| **Overlay Text** | [Text hiển thị] |
| **Subtitle** |同步 narration |
| **Sound** | [Âm thanh] |
| **Transition** | [Chuyển cảnh] |
| **Duration** | XXs |
| **Source** | [Nguồn tham khảo] |
| **Quality Checklist** | [✓] check items |
```

## Timing Calculation

```
Duration = Word Count / 2
(120 words/min = 2 words/sec)

Ví dụ:
  Narration: 72 từ
  Duration: 72 / 2 = 36s

  KHÔNG ước tính. PHẢI tính từ word count.
```

## Factual Writing

| ❌ Không nên | ✅ Nên |
|-------------|--------|
| "AI rất thông minh" | "AI đạt 94% accuracy" |
| "Công nghệ phát triển" | "Số lượng paper tăng 300%" |
| "AI giống bộ não" | "AI đếm xác suất, không hiểu" |

**Mỗi con số PHẢI có nguồn:**
- "94% — Nature, 2020"
- "300% — arXiv statistics"
- "85 triệu — WEF 2020"

## Negative Prompt (Always)

```
blurry, distorted hands, extra fingers, text overlay,
watermark, low quality, cartoon, anime, deformed faces
```

## Quality Check

- [ ] Subject specific (not "a person")?
- [ ] Environment detailed?
- [ ] Action clear?
- [ ] Camera defined?
- [ ] Lighting described?
- [ ] Color specified?
- [ ] Style consistent?
- [ ] **Word count included?**
- [ ] **Duration calculated?**
- [ ] **Source cited?**

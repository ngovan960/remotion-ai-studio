# Documentary Prompt Rules (Nâng Cấp)

## Core Principle

Mỗi prompt PHẢI trả lời 8 câu hỏi + có timing chính xác

## Timing Rule (QUAN TRỌNG)

```
Duration = Word Count / 2
(120 words/min = 2 words/sec)

KHÔNG ước tính.
PHẢI tính từ word count.
Mỗi scene PHẢI có word count rõ ràng.
```

## Prompt Template

```
[Subject] + [Action] + [Environment] + [Camera] + [Lighting] + [Style] + [Color] + [Negative]
```

## Style Keywords by Topic

| Topic | Keywords |
|-------|----------|
| History | `cinematic, 35mm grain, warm earth tones, sepia, vintage` |
| Science | `futuristic, blue neon, volumetric light, clean, modern` |
| Nature | `natural light, organic, earth tones, wide landscape` |
| Technology | `sleek, minimal, blue accents, clean lines` |

## Factual Writing Rules

| ❌ Không nên | ✅ Nên |
|-------------|--------|
| "AI rất thông minh" | "AI đạt 94% accuracy" |
| "Công nghệ phát triển nhanh" | "Số lượng paper tăng 300% từ 2020-2025" |
| "AI giống bộ não" | "AI đếm xác suất, không hiểu" |
| "AI là công cụ" | "Bạn muốn AI làm gì?" |

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

- [ ] Subject specific?
- [ ] Environment detailed?
- [ ] Action clear?
- [ ] Camera defined?
- [ ] Lighting described?
- [ ] Color specified?
- [ ] Style consistent?
- [ ] **Word count included?**
- [ ] **Duration calculated?**
- [ ] **Source cited?**

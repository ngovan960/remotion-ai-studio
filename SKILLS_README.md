# Skills Structure

## General Skills (`skills/`)

Dùng cho TẤT CẢ các loại video:

```
skills/
├── audio-design.md          ← Âm thanh chung
├── broll.md                 ← B-roll planning
├── character-consistency.md ← Nhân vật
├── cinematography.md        ← Quay phim
├── color-theory.md          ← Màu sắc
├── composition.md           ← Sắp xếp khung hình
├── continuity.md            ← Nhất quán
├── documentation.md         ← Hướng dẫn
├── environment-design.md    ← Bối cảnh
├── export-render.md         ← Xuất file
├── scene-segmentation.md    ← Chia scene
├── storytelling.md          ← Kể chuyện
├── transition.md            ← Chuyển cảnh
├── visual-metaphor.md       ← Ẩn dụ trực quan
└── youtube-retention.md     ← YouTube retention
```

## Documentary Pack (`domains/documentary_pack/skills/`)

Dùng CHO RIÊNG documentary:

```
domains/documentary_pack/
├── manifest.yaml            ← Config
├── asset_rules.md           ← Quy tắc asset
├── audio_rules.md           ← Quy tắc audio
├── camera_rules.md          ← Quy tắc camera
├── prompt_rules.md          ← Quy tắc prompt
├── quality_rules.md         ← Quality gates
├── render_rules.md          ← Quy tắc render
└── skills/                  ← 15 documentary skills
    ├── voiceover-writing.md
    ├── prompt-awareness.md
    ├── quality-check.md
    ├── technical-writing.md
    ├── teaching.md
    ├── information-architecture.md
    ├── diagram-thinking.md
    ├── visual-thinking.md
    ├── code-presentation.md
    ├── motion-design.md
    ├── quiz-generation.md
    ├── research.md
    ├── subtitle.md
    ├── thumbnail.md
    └── seo-title.md
```

## Cách Dùng

```
Khi làm video chung → Dùng skills/
Khi làm documentary  → Dùng domains/documentary_pack/skills/
```

## AI Trỏ Đến Đúng Folder

```
User: "Tạo video documentary về AI"
AI: → Load domains/documentary_pack/ (config + skills)
    → Dùng 15 documentary skills
    → Áp dụng documentary rules

User: "Tạo video education về Python"
AI: → Load domains/education/ (config)
    → Dùng skills/ (general skills)
    → Áp dụng education rules
```

# Character Consistency Skill

> Đảm bảo nhân vật nhất quán xuyên suốt video

## Character Attributes

| Attribute | Required | Example |
|-----------|----------|---------|
| Age | ✅ | 28-30 |
| Gender | ✅ | Female |
| Hair | ✅ | Black, long, straight |
| Clothing | ✅ | Blue hoodie, dark jeans |
| Accessories | ✅ | Round glasses, silver watch |
| Expression | ✅ | Calm, determined |
| Build | ✅ | Slim, average height |
| Skin tone | ✅ | Light, warm |

## Character Sheet Template

```markdown
## CHARACTER: [Name]

| Attribute | Description |
|-----------|-------------|
| Age | 28-30 |
| Gender | Female |
| Hair | Black, long, straight |
| Clothing | Blue hoodie, dark jeans, white sneakers |
| Accessories | Round glasses, silver watch |
| Expression | Calm, determined |
| Build | Slim, 165cm |
| Skin | Light, warm tone |

### Prompt Copy-Paste:
"A 28-year-old woman with long straight black hair, wearing a 
blue hoodie and dark jeans, round glasses, silver watch, 
calm expression, cinematic lighting, realistic style"

### Consistency Rules:
- NEVER change face structure
- NEVER change hair style/color
- NEVER change clothing mid-scene
- NEVER change accessories
- Use same seed for all scenes
- Use reference image as anchor
```

## Consistency Techniques

### 1. Reference Image
```python
# Generate ONE high-quality reference
reference = generate_reference(character_prompt, seed=42)

# Use for ALL scenes
for scene in scenes:
    image = img2img(reference, prompt, strength=0.5, seed=42)
```

### 2. Seed Control
```python
CHARACTER_SEED = 42  # Fixed seed for character
# Use same seed for all scenes with this character
```

### 3. Prompt Consistency
```python
# Character description stays EXACTLY the same
CHARACTER = "28yo woman, black long hair, blue hoodie, glasses"
# Every prompt includes this description
```

## Quality Check

- [ ] Character looks same in all scenes?
- [ ] Hair style/color consistent?
- [ ] Clothing unchanged?
- [ ] Accessories present?
- [ ] Expression matches emotion?
- [ ] Same seed used?

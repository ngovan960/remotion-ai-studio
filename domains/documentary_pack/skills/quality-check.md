# Quality Check Skill (Nâng Cấp)

> Kiểm tra TRƯỚC khi xuất bản — bao gồm timing validation

## Timing Validation (QUAN TRỌNG NHẤT)

```python
def validate_timing(scenes):
    """Kiểm tra timing có khớp với word count không"""
    for scene in scenes:
        word_count = len(scene["narration"].split())
        expected_duration = word_count / 2  # 120 words/min = 2 words/sec
        actual_duration = scene["duration"]
        
        if abs(expected_duration - actual_duration) > 5:
            return False, f"Scene {scene['id']}: {word_count} từ = {expected_duration}s, nhưng duration = {actual_duration}s"
    
    return True, "Timing OK"
```

## Checklist Before Export

### 1. Timing Check
- [ ] Mỗi scene có word count?
- [ ] Duration = word count / 2?
- [ ] Tổng duration khớp target?

### 2. Content Check
- [ ] Mỗi statistic có nguồn?
- [ ] Không có claim chưa verify?
- [ ] Hook đủ mạnh (specific, personal)?
- [ ] Không có ChatGPT-style language?

### 3. Production Check
- [ ] Mỗi scene có Goal?
- [ ] Mỗi scene có Key Message?
- [ ] Mỗi scene có Visual Objective?
- [ ] Mỗi scene có Primary Asset?
- [ ] Mỗi scene có Camera Motion?
- [ ] Mỗi scene có Animation?
- [ ] Mỗi scene có Overlay Text?
- [ ] Mỗi scene có Sound?
- [ ] Mỗi scene có Transition?

### 4. Asset Check
- [ ] Asset allocation hợp lý?
- [ ] Stock footage cần thiết đã có?
- [ ] AI-generated assets có prompt đầy đủ?

### 5. Audio Check
- [ ] Voice-over timing khớp scenes?
- [ ] Music mood match scenes?
- [ ] SFX timing correct?

## Timing Validation Script

```python
def validate_documentary(script):
    errors = []
    
    # Check each scene
    for scene in script["scenes"]:
        # Timing check
        word_count = len(scene["narration"].split())
        expected = word_count / 2
        actual = scene["duration"]
        
        if abs(expected - actual) > 5:
            errors.append(f"Scene {scene['id']}: {word_count} từ = {expected}s, nhưng duration = {actual}s")
        
        # Source check
        if not scene.get("source"):
            errors.append(f"Scene {scene['id']}: Không có nguồn tham khảo")
        
        # Production check
        required_fields = ["goal", "key_message", "visual", "primary_asset", "camera", "animation", "sound", "transition"]
        for field in required_fields:
            if not scene.get(field):
                errors.append(f"Scene {scene['id']}: Thiếu {field}")
    
    # Total duration check
    total_words = sum(len(s["narration"].split()) for s in script["scenes"])
    total_expected = total_words / 2
    total_actual = sum(s["duration"] for s in script["scenes"])
    
    if abs(total_expected - total_actual) > 30:
        errors.append(f"Tổng duration: {total_expected}s (tính từ word count) vs {total_actual}s (set)")
    
    return errors
```

## Quality Score Calculation

```python
def calculate_score(script):
    checks = {
        "timing_valid": validate_timing(script["scenes"]),
        "all_sources": all(s.get("source") for s in script["scenes"]),
        "all_goals": all(s.get("goal") for s in script["scenes"]),
        "all_visuals": all(s.get("visual") for s in script["scenes"]),
        "hook_strength": check_hook(script["scenes"][0]),
        "factual_writing": check_factual(script),
    }
    
    passed = sum(1 for v in checks.values() if v)
    total = len(checks)
    
    return passed / total, checks
```

## Export Checklist

- [ ] Timing validated (word count = duration)?
- [ ] All sources cited?
- [ ] All scenes have production metadata?
- [ ] Hook is specific and personal?
- [ ] Writing is factual, not poetic?
- [ ] Asset allocation reasonable?
- [ ] Audio sync with scenes?

# Documentary Quality Rules

## Quality Gates

Pipeline KHÔNG render nếu không pass quality checks.

### Gate 1: Prompt Quality

| Check | Minimum | Weight |
|-------|---------|--------|
| Subject specificity | 7/10 | High |
| Environment detail | 7/10 | High |
| Action clarity | 7/10 | High |
| Camera defined | 6/10 | Medium |
| Lighting described | 6/10 | Medium |
| Color specified | 6/10 | Medium |
| Style consistent | 7/10 | High |
| Negative prompt | Required | Critical |

### Gate 2: Asset Quality

| Check | Minimum | Weight |
|-------|---------|--------|
| Resolution | ≥ 1080p | Critical |
| No artifacts | 8/10 | High |
| Style consistency | 8/10 | High |
| Lighting correct | 7/10 | Medium |
| Color accurate | 7/10 | Medium |

### Gate 3: Audio Quality

| Check | Minimum | Weight |
|-------|---------|--------|
| Voice clarity | 7/10 | High |
| Music mood match | 7/10 | High |
| SFX timing | 6/10 | Medium |
| No audio overlap | Required | Critical |
| Silence used | 6/10 | Medium |

### Gate 4: Continuity

| Check | Minimum | Weight |
|-------|---------|--------|
| Character consistent | Required | Critical |
| Environment consistent | Required | Critical |
| Color palette maintained | 8/10 | High |
| Camera smooth | 7/10 | Medium |
| Timeline logical | Required | Critical |

### Gate 5: Render Quality

| Check | Minimum | Weight |
|-------|---------|--------|
| Resolution correct | Required | Critical |
| FPS correct | Required | Critical |
| Ken Burns smooth | 7/10 | Medium |
| Transitions clean | 7/10 | Medium |
| Subtitles readable | 6/10 | Medium |

## Scoring

```python
def calculate_score(checks):
    weights = {"critical": 3, "high": 2, "medium": 1, "low": 0.5}
    total = sum(checks[c]["score"] * weights[check[c]["weight"]] for c in checks)
    max_possible = sum(10 * weights[check[c]["weight"]] for c in checks)
    return total / max_possible
```

## Pass/Fail Criteria

| Score | Result | Action |
|-------|--------|--------|
| ≥ 0.85 | PASS | Proceed to render |
| 0.70-0.84 | WARNING | Fix issues, re-check |
| < 0.70 | FAIL | Must fix before render |

## Quality Report

```json
{
  "prompt_score": 0.88,
  "asset_score": 0.85,
  "audio_score": 0.82,
  "continuity_score": 0.90,
  "render_score": 0.87,
  "total_score": 0.86,
  "status": "PASS",
  "issues": []
}
```

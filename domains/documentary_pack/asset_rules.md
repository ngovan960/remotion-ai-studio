# Documentary Asset Rules

## Asset Priority

```
1. REUSE    → Dùng lại asset đã có
2. CACHE    → Lấy từ cache
3. STOCK    → Dùng stock footage/ảnh
4. GENERATE → Tạo mới bằng AI
```

## Asset Types by Scene

| Scene Type | Primary Asset | Secondary | Stock OK? |
|------------|---------------|-----------|-----------|
| **Establishing** | Image (wide) | Stock footage | ✅ Yes |
| **Character intro** | Image (portrait) | - | ❌ No |
| **Action scene** | Video clip | Image + Ken Burns | ✅ Yes |
| **Data/Stats** | Chart/Infographic | Image | ❌ No |
| **Timeline** | Timeline graphic | Images | ❌ No |
| **Map** | Map visualization | Stock aerial | ✅ Yes |
| **Transition** | Stock footage | Image + fade | ✅ Yes |
| **Detail** | Image (close-up) | - | ❌ No |
| **Conclusion** | Image (wide) | Stock | ✅ Yes |

## Asset Allocation (per minute)

| Asset Type | Percentage | Count |
|------------|------------|-------|
| Images | 50% | 3 |
| Stock footage | 30% | 2 |
| Video clips | 15% | 1 |
| Charts/Graphics | 5% | 0.3 |
| **Total** | 100% | ~6 |

## Stock Footage Sources

| Source | Type | Cost |
|--------|------|------|
| Pexels | Video + Image | Free |
| Pixabay | Video + Image | Free |
| Unsplash | Image | Free |
| Archive.org | Historical | Free |
| NASA | Space/Science | Free |

## Generate Rules

| When | Model | Settings |
|------|-------|----------|
| Character needed | Flux.1 Dev | 1024x768, steps=28 |
| Environment needed | Flux.1 Dev | 1024x768, steps=28 |
| Action scene | Wan 2.2 | 720p, 81 frames |
| Chart/Infographic | Flux.1 Dev | 1024x768, steps=28 |

## Asset Quality Checklist

- [ ] Resolution ≥ 1080p?
- [ ] No artifacts/distortion?
- [ ] Consistent style?
- [ ] Proper lighting?
- [ ] Correct color palette?

# Documentation Skill

> Hướng dẫn sử dụng và maintain

## File Structure

```
remotion_ai_studio/
├── agents/          ← AI Agents (6)
├── models/          ← Model wrappers (2)
├── pipeline/        ← Pipeline management (3)
├── skills/          ← Skills (20)
├── assets/          ← Generated assets
├── metadata/        ← Configuration
├── cache/           ← Cache system
└── output/          ← Final output
```

## Quick Reference

| Task | Command |
|------|---------|
| Run pipeline | `python pipeline/orchestrator.py --topic "Topic" --duration 10` |
| Check cache | `python -c "from pipeline.cache_manager import CacheManager; ..."` |
| View prompts | `cat assets/json/prompts.json` |
| View story | `cat metadata/story.json` |

## Adding New Skill

1. Create `skills/new-skill.md`
2. Document: Purpose, Rules, Examples, Quality Check
3. Create agent in `agents/new_agent.py`
4. Integrate in `pipeline/orchestrator.py`

## Adding New Model

1. Create `models/new_model.py`
2. Implement: `load()`, `generate()`
3. Add to orchestrator
4. Update documentation

## Maintenance

| Task | Frequency |
|------|-----------|
| Clear cache | Weekly |
| Update dependencies | Monthly |
| Check model updates | Monthly |
| Review skills | Quarterly |

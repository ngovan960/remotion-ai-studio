# Remotion AI Studio

> AI Video Production Pipeline — tự sản xuất video hoàn chỉnh với AI agents, RTX 3090, và Remotion.

---

## Overview

Remotion AI Studio là hệ thống AI tự động sản xuất video, bao gồm:

- **7 AI Agents** — Story, Scene, Prompt, Continuity, Visual Thinking, Voiceover
- **4 AI Models** — Flux (image), Wan (video), Fish Speech (TTS), MusicGen (music)
- **50+ Skills** — cinematography, storytelling, audio design, visual effects...
- **25 Domain Packs** — documentary, education, history, horror
- **Remotion** — React-based video rendering với Ken Burns, crossfade, subtitles

```
Topic → Story → Scenes → Prompts → Assets → Render → Video
```

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/yourusername/remotion-ai-studio.git
cd remotion-ai-studio

# 2. Setup (installs everything)
chmod +x setup.sh
./setup.sh

# 3. Activate environment
source .venv/bin/activate

# 4. Run
python main.py --topic "History of AI" --duration 60
```

---

## Usage

### Basic

```bash
python main.py --topic "Quantum Computing" --duration 120
```

### With MiMo Code

```bash
# Launch MiMo Code
mimo

# Then ask:
"Create a 5-minute documentary about the history of artificial intelligence"
"Generate a horror story video about haunted technology"
"Make an educational video about quantum computing basics"
```

### Remotion Rendering

```bash
npm run start       # Open Remotion Studio (preview)
npm run build       # Render final video
```

---

## Project Structure

```
remotion_ai_studio/
├── core/                    # ProjectManager, Classifier, Planner, Scheduler, QualityGate
├── domains/                 # Domain packs (documentary, education, history, horror)
├── capabilities/            # Capability packs (chart, code, diagram, map, etc.)
├── services/                # AssetStrategy, QualityPolicy, CacheService
├── skills/                  # 50+ AI skills (cinematography, storytelling, etc.)
├── models/                  # AI model wrappers (Flux, Wan)
├── src/                     # Remotion components (Root.tsx, Video.tsx)
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
└── package.json             # Node.js dependencies (Remotion)
```

---

## Pipeline

```
┌─────────────────────────────────────────────────────┐
│  STAGE 1: CLASSIFY & PLAN                          │
│  StoryAgent → ScenePlanner → PromptAgent            │
│  Output: story.json, scene_plan.json, prompts.json  │
├─────────────────────────────────────────────────────┤
│  STAGE 2: ASSET RESOLUTION                         │
│  AssetStrategy: reuse/cache/generate                │
│  Flux → Images, Wan → Video, Fish → Audio           │
├─────────────────────────────────────────────────────┤
│  STAGE 3: QUALITY GATES                            │
│  QualityPolicy: validate all pipeline output        │
├─────────────────────────────────────────────────────┤
│  STAGE 4: RENDER                                   │
│  Remotion + FFmpeg: Ken Burns, crossfade, subs      │
│  Output: final.mp4 (1920x1080, 30fps)              │
└─────────────────────────────────────────────────────┘
```

---

## Deploy on Vast.ai

### 1. Rent a GPU instance

- Go to [vast.ai](https://vast.ai)
- Filter: RTX 3090, 24GB VRAM, Ubuntu 22.04
- Cost: ~$0.30/hr

### 2. Setup instance

```bash
# SSH into instance
ssh root@<instance-ip>

# Clone and setup
git clone https://github.com/yourusername/remotion-ai-studio.git
cd remotion-ai-studio
chmod +x setup.sh
./setup.sh
```

### 3. Run pipeline

```bash
source .venv/bin/activate
python main.py --topic "History of AI" --duration 300
```

### 4. Download result

```bash
# From local machine
scp root@<instance-ip>:/root/remotion_ai_studio/output/final.mp4 .
```

---

## Requirements

| Component | Version |
|-----------|---------|
| Python | 3.10+ |
| Node.js | 20+ |
| GPU | RTX 3090 (24GB VRAM) |
| RAM | 32GB+ |
| Storage | 50GB+ |

---

## Cost

| Item | Value |
|------|-------|
| GPU (Vast.ai) | $0.30/hr |
| Pipeline time | ~35 min |
| Total cost | ~$0.18 |
| Output | 1920x1080, 30fps |

---

## License

MIT
# remotion-ai-studio

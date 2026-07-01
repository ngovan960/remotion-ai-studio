#!/bin/bash
set -e

echo "=========================================="
echo "  Remotion AI Studio - Production Setup"
echo "=========================================="

# ─────────────────────────────────────────
# HF TOKEN
# ─────────────────────────────────────────
if [ -z "$HF_TOKEN" ]; then
  echo "Warning: HF_TOKEN is not set. Please set it in your terminal before running: export HF_TOKEN='your_token'"
fi

# ─────────────────────────────────────────
# Python check
# ─────────────────────────────────────────
echo ""
echo "[1/6] Checking Python..."
python3 --version

# ─────────────────────────────────────────
# Node.js (nvm)
# ─────────────────────────────────────────
echo ""
echo "[2/6] Setting up Node.js..."

if ! command -v node &>/dev/null; then
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
  export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
  nvm install 20
  nvm use 20
fi

echo "Node: $(node -v)"

# ─────────────────────────────────────────
# Python venv
# ─────────────────────────────────────────
echo ""
echo "[3/6] Python environment..."

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate

pip install --upgrade pip -q
pip install -r requirements.txt -q

# Install gguf for loading GGUF models in diffusers
pip install gguf -q

# install HF CLI mới
pip install -U huggingface_hub -q

# ─────────────────────────────────────────
# Node deps
# ─────────────────────────────────────────
echo ""
echo "[4/6] Node dependencies..."
npm install --silent

# ─────────────────────────────────────────
# Folders
# ─────────────────────────────────────────
echo ""
echo "[5/6] Creating folders..."

mkdir -p assets/{images,videos,audio,subtitles,json}
mkdir -p metadata cache output
mkdir -p modelAI/{flux,wan,fish,musicgen,audiogen}

# ─────────────────────────────────────────
# MODELS DOWNLOAD (OFFICIAL HUGGINGFACE-CLI)
# ─────────────────────────────────────────
echo ""
echo "[6/6] Downloading models (Phương án 1: Chất lượng Tuyệt đối)..."

# FLUX (GGUF - LIGHT & FAST)
echo "→ FLUX.1-dev (GGUF Q8 + VAE + Text Encoders)..."
hf download lllyasviel/FLUX.1-dev-gguf \
  --exclude "*Q2_K*" "*Q3_K*" "*Q4_K*" "*Q5_K*" "*Q6_K*" "*Q8_1*" "*schnell*" "*F16.gguf" "*t5xxl_fp16.safetensors*" \
  --local-dir modelAI/flux 

# WAN 2.2 5B (Chất lượng Tuyệt đối)
echo "→ Wan 2.2 5B (FP8 optimized)..."
hf download shunyang90/Wan2.2-TI2V-5B-ModelOpt-FP8 \
  --local-dir modelAI/wan 

# Fish Speech
echo "→ Fish Speech 1.5..."
hf download fishaudio/fish-speech-1.5 \
  --local-dir modelAI/fish 

# MusicGen (Large - Chất lượng Tuyệt đối)
echo "→ MusicGen Large..."
hf download facebook/musicgen-large \
  --exclude "*.safetensors" "pytorch_model*" \
  --local-dir modelAI/musicgen 

# AudioGen
echo "→ AudioGen medium..."
hf download facebook/audiogen-medium \
  --local-dir modelAI/audiogen 

echo ""
echo "=========================================="
echo "  ✅ Setup Complete"
echo "=========================================="

echo ""
echo "Model sizes:"
du -sh modelAI/*/

echo ""
echo "Run:"
echo "  source .venv/bin/activate"
echo "  npm run dev"
echo "  mimo"

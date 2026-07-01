#!/bin/bash
# setup.sh — Full setup for Remotion AI Studio
# Requires: Ubuntu 20.04+, sudo access for system deps

set -e

echo "=========================================="
echo "  Remotion AI Studio - Full Setup"
echo "=========================================="

# ── Check OS ──────────────────────────────
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
  echo "⚠  This script is designed for Linux. Adapt manually for macOS/Windows."
fi

# ── System dependencies ───────────────────
echo ""
echo "Installing system dependencies..."
sudo apt-get update -qq
sudo apt-get install -y -qq curl wget git build-essential ffmpeg

# ── Python 3.10+ ─────────────────────────
echo ""
echo "Checking Python..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "  Found: Python $PYTHON_VERSION"

if ! python3 -c "import sys; assert sys.version_info >= (3, 10)" 2>/dev/null; then
  echo "  Python 3.10+ required. Installing Python 3.12..."
  sudo add-apt-repository -y ppa:deadsnakes/ppa
  sudo apt-get update -qq
  sudo apt-get install -y -qq python3.12 python3.12-venv python3.12-dev
fi

# ── Node.js 20+ ──────────────────────────
echo ""
echo "Checking Node.js..."
if command -v node &>/dev/null; then
  NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
  echo "  Found: Node.js v$(node -v)"
  if [ "$NODE_VERSION" -lt 20 ]; then
    echo "  Node.js 20+ required. Installing..."
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y -qq nodejs
  fi
else
  echo "  Installing Node.js 20..."
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
  sudo apt-get install -y -qq nodejs
fi
echo "  Node.js: $(node -v)"

# ── MiMo Code ────────────────────────────
echo ""
echo "Installing MiMo Code..."
if ! command -v mimo &>/dev/null; then
  curl -fsSL https://mimo.xiaomi.com/install | bash
  echo "  ⚠  Add to PATH: export PATH=\"\$HOME/.local/bin:\$PATH\""
else
  echo "  MiMo Code already installed: $(mimo --version 2>/dev/null || echo 'installed')"
fi

# ── Python virtual environment ───────────
echo ""
echo "Setting up Python virtual environment..."
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "  Created .venv/"
fi
source .venv/bin/activate

# ── Python dependencies ──────────────────
echo ""
echo "Installing Python dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "  Python deps installed."

# ── Node.js dependencies ─────────────────
echo ""
echo "Installing Node.js dependencies..."
npm install --silent
echo "  Node.js deps installed."

# ── Create .env ──────────────────────────
if [ ! -f .env ]; then
  cp .env.example .env
  echo "  Created .env from .env.example"
fi

# ── Create directories ───────────────────
mkdir -p assets/{images,videos,audio,subtitles,json}
mkdir -p metadata cache output

# ── Download AI models ───────────────────
echo ""
echo "Downloading AI models (~20GB total)..."
echo "  This may take a while on first run."

# Create model directory
mkdir -p modelAI/{flux,wan,fish,musicgen}

# Flux.1 Dev (image generation)
echo "  → Flux.1 Dev (~12GB)..."
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('black-forest-labs/FLUX.1-dev', local_dir='modelAI/flux')
" 2>/dev/null || echo "  ⚠  Flux download failed — will download on first use"

# Wan 2.1 (video generation)
echo "  → Wan 2.1 (~5GB)..."
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('Wan-AI/Wan2.1-T2V-14B', local_dir='modelAI/wan')
" 2>/dev/null || echo "  ⚠  Wan download failed — will download on first use"

# Fish Speech (TTS)
echo "  → Fish Speech (~2GB)..."
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('fishaudio/fish-speech-1.5', local_dir='modelAI/fish')
" 2>/dev/null || echo "  ⚠  Fish download failed — will download on first use"

# MusicGen (music)
echo "  → MusicGen (~3GB)..."
python3 -c "
from huggingface_hub import snapshot_download
snapshot_download('facebook/musicgen-small', local_dir='modelAI/musicgen')
" 2>/dev/null || echo "  ⚠  MusicGen download failed — will download on first use"

# ── Summary ──────────────────────────────
echo ""
echo "=========================================="
echo "  ✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Activated virtual environment: .venv/"
echo ""
echo "Quick start:"
echo "  source .venv/bin/activate"
echo "  python main.py --topic 'History of AI' --duration 60"
echo ""
echo "Remotion (video rendering):"
echo "  npm run start      # Open Remotion Studio"
echo "  npm run build      # Render final video"
echo ""
echo "MiMo Code integration:"
echo "  mimo               # Launch MiMo Code"
echo "  # Then ask: 'Create a documentary about quantum computing'"

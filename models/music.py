#!/usr/bin/env python3
"""
MusicGen Wrapper
Local music generation model
"""
import torch
import soundfile as sf
from pathlib import Path

class MusicGenModel:
    def __init__(self, model_name="modelAI/musicgen"):
        if not Path(model_name).exists():
            model_name = "facebook/musicgen-large"
        self.model_name = model_name
        self.model = None
    
    def load(self):
        """Load MusicGen model"""
        print(f"Loading MusicGen from {self.model_name}...")
        try:
            from audiocraft.models import MusicGen
            self.model = MusicGen.get_pretrained(self.model_name)
            print("MusicGen loaded!")
        except Exception as e:
            print(f"Error loading MusicGen: {e}")
            raise
    
    def generate(self, prompt, output_path, duration=30):
        """Generate music from text prompt"""
        if self.model is None:
            self.load()
        
        print(f"  Generating {duration}s of music...")
        print(f"  Prompt: {prompt}")
        
        self.model.set_generation_params(duration=duration)
        
        wav = self.model.generate([prompt])
        
        sf.write(str(output_path), wav[0].cpu().numpy(), 32000)
        
        print(f"  Saved: {output_path}")
        return output_path
 
MUSICGEN_INFO = {
    "name": "MusicGen Large",
    "vram_required": "~6 GB",
    "quality": "⭐⭐⭐⭐⭐",
    "speed": "~120s for 30s music",
    "languages": ["text-to-music"],
    "license": "MIT"
}

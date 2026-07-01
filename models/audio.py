#!/usr/bin/env python3
"""
AudioGen Wrapper
Local sound effects generation model
"""
import torch
import soundfile as sf
from pathlib import Path

class AudioGenModel:
    def __init__(self, model_name="modelAI/audiogen"):
        if not Path(model_name).exists():
            model_name = "facebook/audiogen-medium"
        self.model_name = model_name
        self.model = None
    
    def load(self):
        """Load AudioGen model"""
        print(f"Loading AudioGen from {self.model_name}...")
        try:
            from audiocraft.models import AudioGen
            self.model = AudioGen.get_pretrained(self.model_name)
            print("AudioGen loaded!")
        except Exception as e:
            print(f"Error loading AudioGen: {e}")
            raise
    
    def generate(self, prompt, output_path, duration=3):
        """Generate sound effect from text prompt"""
        if self.model is None:
            self.load()
        
        print(f"  Generating SFX: {prompt}")
        
        self.model.set_generation_params(duration=duration)
        
        wav = self.model.generate([prompt])
        
        sf.write(str(output_path), wav[0].cpu().numpy(), 32000)
        
        print(f"  Saved: {output_path}")
        return output_path

AUDIOGEN_INFO = {
    "name": "AudioGen Medium",
    "vram_required": "~2-4 GB",
    "quality": "⭐⭐⭐⭐",
    "speed": "~30s for 3s SFX",
    "languages": ["text-to-sfx"],
    "license": "MIT"
}

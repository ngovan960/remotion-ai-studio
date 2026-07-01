#!/usr/bin/env python3
"""
Fish Speech TTS Wrapper
Local TTS model for voice-over generation
"""
import torch
import soundfile as sf
from pathlib import Path

class FishSpeechModel:
    def __init__(self, model_path="modelAI/fish"):
        if not Path(model_path).exists():
            model_path = "fishaudio/fish-speech-1.5"
        self.model_path = model_path
        self.model = None
    
    def load(self):
        """Load Fish Speech model"""
        print(f"Loading Fish Speech from {self.model_path}...")
        try:
            from fish_speech import FishSpeech
            self.model = FishSpeech.from_pretrained(self.model_path)
            self.model = self.model.to('cuda')
            print("Fish Speech loaded!")
        except Exception as e:
            print(f"Error loading Fish Speech: {e}")
            raise
    
    def generate(self, text, output_path, voice="M1"):
        """Generate speech from text"""
        if self.model is None:
            self.load()
        
        print(f"  Generating speech...")
        
        audio = self.model.synthesize(text, speaker=voice)
        
        sf.write(str(output_path), audio, 22050)
        
        duration = len(audio) / 22050
        print(f"  Saved: {output_path} ({duration:.1f}s)")
        
        return output_path

FISH_SPEECH_INFO = {
    "name": "Fish Speech 1.5",
    "vram_required": "~1-2 GB",
    "quality": "⭐⭐⭐⭐",
    "speed": "Real-time",
    "voices": ["M1", "M2", "M3", "F1", "F2", "F3"],
    "languages": ["en", "vi", "zh", "ja", "ko"],
    "license": "Open source"
}

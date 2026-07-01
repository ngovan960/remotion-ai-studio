#!/usr/bin/env python3
"""
Flux Model Wrapper
RTX 3090 optimized image generation
"""
import torch
from diffusers import FluxPipeline, StableDiffusionImg2ImgPipeline
from PIL import Image
from pathlib import Path
import json

class FluxModel:
    def __init__(self, model_path="black-forest-labs/FLUX.1-dev", device="cuda"):
        self.model_path = model_path
        self.device = device
        self.pipe_txt2img = None
        self.pipe_img2img = None
        self.seed = 42
    
    def load(self):
        """Load Flux model"""
        print("Loading Flux.1 Dev...")
        
        self.pipe_txt2img = FluxPipeline.from_pretrained(
            self.model_path,
            torch_dtype=torch.bfloat16
        )
        self.pipe_txt2img = self.pipe_txt2img.to(self.device)
        self.pipe_txt2img.enable_model_cpu_offload()
        
        print("Flux loaded!")
    
    def generate(self, prompt, output_path, width=1024, height=768, 
                 steps=28, guidance=3.5, seed=None):
        """Generate image"""
        if self.pipe_txt2img is None:
            self.load()
        
        gen_seed = seed or self.seed
        
        image = self.pipe_txt2img(
            prompt=prompt,
            negative_prompt="blurry, low quality, distorted, watermark",
            num_inference_steps=steps,
            guidance_scale=guidance,
            width=width,
            height=height,
            generator=torch.Generator().manual_seed(gen_seed)
        ).images[0]
        
        image.save(output_path)
        return image
    
    def generate_with_reference(self, prompt, reference_image, output_path,
                                 strength=0.5, seed=None):
        """Generate image với reference (img2img)"""
        if self.pipe_img2img is None:
            self.pipe_img2img = StableDiffusionImg2ImgPipeline.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16
            )
            self.pipe_img2img = self.pipe_img2img.to(self.device)
        
        gen_seed = seed or self.seed
        
        image = self.pipe_img2img(
            prompt=prompt,
            image=reference_image,
            strength=strength,
            negative_prompt="blurry, distorted, inconsistent",
            num_inference_steps=30,
            guidance_scale=7.5,
            generator=torch.Generator().manual_seed(gen_seed)
        ).images[0]
        
        image.save(output_path)
        return image
    
    def generate_reference(self, character_prompt, output_path):
        """Generate high-quality reference image"""
        return self.generate(
            prompt=f"portrait of {character_prompt}, front view, detailed face, studio lighting",
            output_path=output_path,
            steps=50,  # More steps for quality
            guidance=7.5,
            width=512,
            height=512
        )

# Model info
FLUX_INFO = {
    "name": "Flux.1 Dev",
    "vram_required": "12GB (FP8)",
    "quality": "⭐⭐⭐⭐⭐",
    "speed": "~8s per image",
    "best_for": "High-quality image generation"
}

#!/usr/bin/env python3
"""
Wan 2.2 5B Model Wrapper
RTX 3090 optimal balance: quality + speed + VRAM
"""
import torch
from PIL import Image
from pathlib import Path
import imageio

class WanModel:
    def __init__(self, model_path="modelAI/wan", device="cuda"):
        if not Path(model_path).exists():
            model_path = "Wan-AI/Wan2.2-TI2V-5B"
        self.model_path = model_path
        self.device = device
        self.pipe = None
    
    def load(self):
        """Load Wan 2.2 5B model - optimal for RTX 3090"""
        print(f"Loading Wan 2.2 5B from {self.model_path}...")
        
        from diffusers import WanPipeline
        
        self.pipe = WanPipeline.from_pretrained(
            self.model_path,
            torch_dtype=torch.bfloat16
        )
        
        # Cast transformer to FP8 (float8_e4m3fn) to match FP8 VRAM usage (~10 GB)
        if hasattr(self.pipe, "transformer"):
            print("  Quantizing Wan transformer to FP8 (float8_e4m3fn)...")
            self.pipe.transformer.to(torch.float8_e4m3fn)
            
        self.pipe = self.pipe.to(self.device)
        
        # RTX 3090 optimizations
        self.pipe.enable_model_cpu_offload()
        
        print("Wan 2.2 5B loaded!")
        print("  Mode: FP8")
        print("  VRAM: ~10-12 GB (comfortable on RTX 3090 24GB)")
        print("  Features: Text + Image to Video (TI2V)")
    
    def generate(self, image_path, prompt, output_path, 
                 num_frames=81, num_steps=30, resolution="720p"):
        """
        Generate video clip from image
        
        Args:
            image_path: Input image path
            prompt: Motion description
            output_path: Output video path
            num_frames: Number of frames (81 = 3.4s @ 24fps)
            num_steps: Inference steps
            resolution: "480p" or "720p"
        """
        if self.pipe is None:
            self.load()
        
        print(f"  Generating video ({resolution}, {num_frames} frames)...")
        
        image = Image.open(image_path)
        
        # Resolution settings
        if resolution == "720p":
            width, height = 1280, 720
        else:  # 480p
            width, height = 854, 480
        
        # Resize image
        image = image.resize((width, height))
        
        # Generate video
        video = self.pipe(
            prompt=prompt,
            image=image,
            num_frames=num_frames,
            num_inference_steps=num_steps,
            guidance_scale=5.0,
            width=width,
            height=height,
        ).frames[0]
        
        # Save
        imageio.mimsave(str(output_path), video, fps=24)
        
        file_size = Path(output_path).stat().st_size / (1024 * 1024)
        print(f"  Saved: {output_path} ({file_size:.1f} MB)")
        
        return output_path
    
    def generate_batch(self, items, output_dir, resolution="720p"):
        """Generate multiple video clips"""
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if self.pipe is None:
            self.load()
        
        results = []
        for i, item in enumerate(items, 1):
            output_path = output_dir / f"clip_{i:03d}.mp4"
            print(f"[{i}/{len(items)}] Generating clip...", end=" ", flush=True)
            
            self.generate(
                item["image"],
                item["prompt"],
                output_path,
                resolution=resolution
            )
            results.append(str(output_path))
            print("done")
        
        return results

# Model Info
WAN_INFO = {
    "name": "Wan 2.2 TI2V-5B",
    "vram_required": "10-12 GB (FP8)",
    "quality": "⭐⭐⭐⭐",
    "speed": "~45-60s per clip",
    "resolution": "720p",
    "best_for": "Balanced quality/speed on RTX 3090",
    "license": "Apache 2.0",
    "features": "Text + Image to Video (TI2V)"
}

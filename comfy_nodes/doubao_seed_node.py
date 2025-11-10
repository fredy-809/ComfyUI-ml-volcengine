"""
Author: Fredy
Date: 2025-11-08
Description: ComfyUI node for Volcano Engine's Doubao-Seed-1.6 multimodal model
"""

import json
import os
import base64
from io import BytesIO
from PIL import Image
import requests
import torch
import numpy as np

class DoubaoSeedNode:
    def __init__(self):
        self.api_endpoint = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "system_prompt": ("STRING", {
                    "multiline": True,
                    "default": "你是一个专业的图像分析专家，请对图片内容进行分析。"
                }),
                "user_prompt": ("STRING", {
                    "multiline": True,
                    "default": "请描述这张图片的内容。"
                }),
                "reasoning_effort": (["minimal", "low", "medium", "high"], {
                    "default": "medium"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "analyze_image"
    CATEGORY = "Volcano/Doubao"

    def encode_image_to_base64(self, image):
        try:
            # ComfyUI images are in format (1, H, W, 3) with values in range 0-1
            if len(image.shape) != 4:
                raise ValueError(f"Expected 4D tensor, got {len(image.shape)}D")
            
            # Convert to numpy and scale to 0-255
            image_np = (image[0].cpu().numpy() * 255).clip(0, 255).astype('uint8')
            
            # Create PIL image directly from numpy array (already in HWC format)
            pil_image = Image.fromarray(image_np, 'RGB')
            
            # Convert PIL Image to base64
            buffered = BytesIO()
            pil_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return img_str
            
        except Exception as e:
            print(f"Image conversion error: {str(e)}")
            print(f"Image shape: {image.shape}, dtype: {image.dtype}, range: [{float(image.min())}, {float(image.max())}]")
            raise

    def analyze_image(self, image, api_key, system_prompt, user_prompt, reasoning_effort):
        try:
            # Encode image to base64
            base64_image = self.encode_image_to_base64(image)
            
            # Prepare the request payload
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            
            payload = {
                "model": "doubao-seed-1-6-251015",
                "max_completion_tokens": 65535,
                "reasoning_effort": reasoning_effort,
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64_image}"
                                }
                            },
                            {
                                "type": "text",
                                "text": user_prompt
                            }
                        ]
                    }
                ]
            }
            
            # Make API request
            response = requests.post(
                self.api_endpoint,
                headers=headers,
                json=payload,
                timeout=300  # 5 minutes timeout
            )
            
            if response.status_code != 200:
                return (f"Error: {response.status_code} - {response.text}",)
                
            result = response.json()
            output = result.get("choices", [{}])[0].get("message", {}).get("content", "No output received")
            return (output,)
            
        except Exception as e:
            return (f"Error occurred: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "DoubaoSeedNode": DoubaoSeedNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DoubaoSeedNode": "Doubao Seed 1.6 Image Analyzer"
}

import os
import base64
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from PIL import Image
import io
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    """Encode image to base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_ollama_ocr_text(model_name, image_path):
    """
    Perform OCR using Ollama models via LangChain.
    Supports multimodal models like gemma3:4b and qwen2.5-vl.
    """
    try:
        llm = ChatOllama(model=model_name, temperature=0)
        
        image_base64 = encode_image(image_path)
        
        message = HumanMessage(
            content=[
                {"type": "text", "text": "Transcribe all the text found in this image. Do not provide any explanations or meta-talk. Just the transcribed text."},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                },
            ]
        )
        
        response = llm.invoke([message])
        return response.content.strip()
    except Exception as e:
        return f"Error with {model_name}: {str(e)}"

def get_gemma3_ocr(image_path):
    """OCR using Gemma 3 4b via Ollama."""
    return get_ollama_ocr_text("gemma3:4b", image_path)

def get_qwen_vl_ocr(image_path):
    """OCR using Qwen 2.5 VL via Ollama."""
    return get_ollama_ocr_text("qwen2.5-vl", image_path)

import os
from ocr_engine import get_gemma3_ocr, get_qwen_vl_ocr
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_images():
    """
    Extract text from all images in the data folder using Gemma 3 and Qwen 2.5 VL
    via Ollama + LangChain and save the results in separate txt files.
    """
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        print(f"Error: {data_dir} directory not found.")
        return
    
    # Find all image files
    images = sorted([f for f in os.listdir(data_dir) 
                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])
    
    if not images:
        print("No images found in data folder.")
        return
    
    models = [
        {"name": "Gemma 3 (4b)", "func": get_gemma3_ocr, "suffix": "gemma3"},
        {"name": "Qwen 2.5 VL", "func": get_qwen_vl_ocr, "suffix": "qwen25"}
    ]
    
    print(f"🚀 Starting OCR text extraction on {len(images)} images using Ollama models...")
    
    for model in models:
        print(f"\n--- Processing with {model['name']} ---")
        for img_name in tqdm(images, desc=f"{model['name']} Extraction"):
            img_path = os.path.join(data_dir, img_name)
            
            try:
                extracted_text = model['func'](img_path)
            except Exception as e:
                extracted_text = f"Error extracting text: {str(e)}"
                print(f"\n⚠ Error processing {img_name}: {str(e)}")
            
            # Create output filename
            base_name = os.path.splitext(img_name)[0]
            output_filename = f"{base_name}_{model['suffix']}_ollama.txt"
            output_path = os.path.join(data_dir, output_filename)
            
            # Save extracted text
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(extracted_text)
    
    print(f"\n✅ OCR extraction complete! Processed {len(images)} images with 2 models.")

if __name__ == "__main__":
    extract_text_from_images()

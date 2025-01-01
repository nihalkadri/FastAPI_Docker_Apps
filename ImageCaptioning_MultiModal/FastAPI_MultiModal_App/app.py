from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

app = FastAPI()

#test123456
# Function to generate a caption using BLIP model
def generate_caption(image: Image.Image) -> str:
    # Preprocess the image and generate caption
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

@app.post("/generate-caption")
async def generate_caption_from_image(image: UploadFile = File(...)):
    try:
        # Convert uploaded image to PIL format
        image_bytes = await image.read()
        image = Image.open(io.BytesIO(image_bytes))
        print(f"Received image: {image.filename}")
        
        # Generate the caption using the model
        caption = generate_caption(image)
        print(f"caption: {caption}")
        
        return JSONResponse(content={"caption": caption})

    except Exception as e:
        return JSONResponse(content={"detail": f"Error processing image: {str(e)}"}, status_code=400)

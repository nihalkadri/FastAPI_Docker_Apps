import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Image Captioning App")
#test
# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

    # Call the FastAPI backend for caption generation
    if st.button("Generate Caption"):
        # Send image to FastAPI backend
        image_bytes = uploaded_image.read()
        response = requests.post("https://nihalk-fastapi-multimodal-app.hf.space/generate-caption", files={"image": image_bytes})

        if response.status_code == 200:
            caption = response.json().get("caption", "No caption generated.")
            st.subheader(f"Generated Caption: {caption}")
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error.')}")

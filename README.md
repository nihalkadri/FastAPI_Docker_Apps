# FastAPI_Docker_Apps
This repository showcases projects that integrate FastAPI, Streamlit, Docker, Hugging Face Spaces, and GitHub Actions for deploying machine learning applications. It demonstrates how these technologies can be combined for scalable and efficient app deployment.

## ImageCaptioning_MultiModal
The ImageCaptioning_MultiModal project is an image captioning application that uses FastAPI for the backend, Streamlit for the frontend, and the BLIP model for generating captions from uploaded images. The entire app is containerized with Docker and deployed on Hugging Face Spaces for easy access. GitHub Actions automates the deployment process.

### **Technologies:**
- **FastAPI**: Backend API to handle image processing and caption generation
- **Streamlit**: Interactive frontend for users to upload images and display captions
- **BLIP model**: Used to generate captions for images
- **Docker**: Containerizes the entire app for easier deployment
- **Hugging Face Spaces**: Platform for deploying and sharing the app
- **GitHub Actions**: Automates the deployment process to **Hugging Face Spaces**, syncing changes made to the **FastAPI backend** and **Streamlit frontend** on GitHub, which are then automatically deployed to Hugging Face Spaces for user access.

### Use Case:
The app generates captions for images, which is useful for content generation, accessibility enhancements, and demos for image captioning models.

import streamlit as st
from PIL import Image
import torch
from torchvision import transforms, models
import torch.nn as nn

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="🔥 Forest Fire Detector", layout="centered")

# Load model
@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(model.fc.in_features, 2)
    model.load_state_dict(torch.load('forest_fire_detector.pth', map_location=device))
    model = model.to(device)
    model.eval()
    return model, device

model, device = load_model()

# Image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# UI Layout
st.markdown("<h1 style='text-align: center;'>🔥 Forest Fire Detection App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload a forest image and detect fire using AI</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')

    # Process and predict
    img_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(img_tensor)
        _, pred = torch.max(output, 1)

    class_names = ["Fire","No Fire"]
    prediction = class_names[pred.item()]

    # Display result with caption
    st.markdown("---")
    st.image(image, caption=f"🧠 Prediction: **{prediction}**", use_container_width =True)
    st.success(f"🔥 Model Prediction: {prediction}")

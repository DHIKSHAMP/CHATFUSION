import torch
from torchvision import models, transforms
from PIL import Image
import requests

def load_image(image_path):
    """Load and preprocess the image."""
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)

def get_class_labels():
    """Load the class labels for ImageNet."""
    url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    response = requests.get(url)
    return response.json()

def recognize_image(image_path):
    """Recognize objects in the image."""
    model = models.resnet50(pretrained=True)
    model.eval()
    
    image_tensor = load_image(image_path)

    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted_idx = torch.max(outputs, 1)

    labels = get_class_labels()
    return labels[predicted_idx.item()]
import easyocr
import cv2

def extract_text_from_image(image_path):
    # Initialize EasyOCR Reader
    reader = easyocr.Reader(['en'])  # 'en' stands for English, you can add more languages like ['en', 'fr', 'de']

    # Read the image
    img = cv2.imread(image_path)

    # Use EasyOCR to extract text from the image
    result = reader.readtext(img)

    # Extract and display the text
    text = ''
    for detection in result:
        text += detection[1] + '\n'

    return text




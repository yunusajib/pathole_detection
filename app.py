import gradio as gr
from ultralytics import YOLO
from PIL import Image, ImageDraw
import numpy as np

# Load your YOLOv8 model
model = YOLO("my_yolo_model.onnx")  # or "yolov8n.pt"

def predict(image):
    # Convert Gradio's numpy array to PIL Image
    pil_image = Image.fromarray(image)
    
    # Run YOLOv8 inference
    results = model(pil_image)
    
    # Extract bounding boxes and labels
    boxes = results[0].boxes.xyxy.cpu().numpy()  # Coordinates
    classes = results[0].boxes.cls.cpu().numpy()  # Class IDs
    confidences = results[0].boxes.conf.cpu().numpy()  # Confidence scores
    
    # Draw bounding boxes on the image (PIL)
    draw = ImageDraw.Draw(pil_image)
    for box, cls, conf in zip(boxes, classes, confidences):
        x1, y1, x2, y2 = box
        label = f"{model.names[int(cls)]} {conf:.2f}"
        
        # Draw rectangle and label
        draw.rectangle([x1, y1, x2, y2], outline="blue", width=2)
        draw.text((x1, y1), label, fill="red")
    
    return pil_image  # Return PIL Image (Gradio handles RGB)

# Gradio Interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(label="Input Image"),
    outputs=gr.Image(label="Detected Objects"),
    title="Pathole Detection by Yunusa Jibrin ",
    examples=["example1.jpg", "example2.jpg"],  # Optional
)

demo.launch()
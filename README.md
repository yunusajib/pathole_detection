# 🕳️ Pothole Detection App with YOLOv8

A lightweight, real-time pothole detection system using YOLOv8 and Gradio. Upload an image, and the system detects potholes with bounding boxes and confidence scores.

🎥 **[Watch Demo Video] https://youtu.be/NlIeVglp-nQ**

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone (https://github.com/yunusajib/pathole_detection.git)
 
cd pothole-detection-yolo
### 2. Install Dependencies

pip install -r requirements.txt
### 3. Run the App

python app.py
The Gradio interface will launch at http://127.0.0.1:7860.

📸 Using the Application
### Step 1: Upload Image
Open the Gradio interface

Upload a road image (sample images provided)

### Step 2: Run Detection
The app processes the image using your YOLOv8 model

Detected potholes are highlighted with blue boxes

Labels show the class name and confidence

### Step 3: View Output
The output image displays bounding boxes for potholes

Confidence scores are shown for each detection

🧠 Model Details
Model: YOLOv8 (ONNX or PyTorch format)

Custom Trained: Yes (trained on pothole images)

Framework: Ultralytics YOLO

Deployment: Gradio web UI

✨ Features
🔍 Real-time pothole detection

📦 ONNX model support for optimized inference

🖼️ Easy-to-use drag-and-drop image interface

🧠 Confidence scores and labels included

🎯 Lightweight and fast

💻 System Requirements
Python 3.8+

8GB RAM minimum (16GB recommended)

GPU recommended for faster inference (optional)

⚠️ Troubleshooting
Issue	Solution
Model loading error	Ensure my_yolo_model.onnx exists and path is correct
No detections shown	Try another image or verify model training quality
Out of memory	Use a smaller YOLO model like yolov8n.onnx

📂 Folder Structure

pothole-detection-yolo/
│
├── app.py                # Main Gradio app
├── my_yolo_model.onnx    # Your YOLOv8 model
├── example1.jpg          # Sample image
├── example2.jpg          # Sample image
└── requirements.txt      # Dependencies
🔮 Next Steps
Replace sample images with real road scenes

Integrate with a video stream or camera

Deploy as a web app or mobile-friendly tool on HuggingFace: https://huggingface.co/spaces/yunusajib/pathole_detection_model

Improve dataset for higher model accuracy

👨‍💻 Author
Yunusa Jibrin
---


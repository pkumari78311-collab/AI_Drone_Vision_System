from ultralytics import YOLO

# Load YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Detect objects in sample image
results = model("https://ultralytics.com/images/bus.jpg", show=True)
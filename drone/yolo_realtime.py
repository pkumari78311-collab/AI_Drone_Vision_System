from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Run webcam detection (0 = default camera)
results = model.predict(source=0, show=True)
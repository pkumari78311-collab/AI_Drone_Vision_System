from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run detection on a sample image
results = model("https://ultralytics.com/images/bus.jpg", show=True)

print("Detection completed!")
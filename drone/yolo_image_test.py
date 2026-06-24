from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run detection on an image
results = model("https://ultralytics.com/images/bus.jpg")

# Show result image with bounding boxes
results[0].show()
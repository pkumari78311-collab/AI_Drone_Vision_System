from ultralytics import YOLO

model = YOLO("yolov8n.pt")

image_path = r"C:\Users\User\Downloads\EdgeAI_Drone_Project\images\car.jpg"

results = model.predict(
    source=image_path,
    save=True
)

print("Detection completed!")

input("Press Enter to close...")
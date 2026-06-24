import airsim
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Connect to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

print("Connected to AirSim!")

while True:

    # Capture image from front camera
    response = client.simGetImage("0", airsim.ImageType.Scene)

    if response is None:
        continue

    # Convert image bytes
    img_array = np.frombuffer(response, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if frame is None:
        continue

    # Run YOLO
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Display
    cv2.imshow("AirSim + YOLO Detection", annotated_frame)

    # Quit with q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
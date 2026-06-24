import airsim
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Connect to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True)
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

# Rise to safe altitude
client.moveToZAsync(-10, 3).join()

frame_width = 640

while True:

    # Get image from drone camera
    response = client.simGetImage("0", airsim.ImageType.Scene)

    if response is None:
        continue

    img_array = np.frombuffer(response, dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if frame is None:
        continue

    # Run YOLO
    results = model(frame)

    annotated_frame = results[0].plot()

    # Process detections
    for box in results[0].boxes:

        x1, y1, x2, y2 = box.xyxy[0]

        object_center_x = (x1 + x2) / 2

        if object_center_x < frame_width/3:

            print("MOVE LEFT")

        elif object_center_x < 2*frame_width/3:

            print("MOVE FORWARD")

        else:

            print("MOVE RIGHT")

    cv2.imshow("YOLO Navigation", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

client.hoverAsync().join()

client.armDisarm(False)
client.enableApiControl(False)
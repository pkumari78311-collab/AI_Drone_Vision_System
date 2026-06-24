import airsim
import cv2
import numpy as np
import time

# Connect to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

# Enable drone control
client.enableApiControl(True)
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

# Rise slightly
client.moveByVelocityAsync(0, 0, -2, 3).join()

# Capture and save 10 images
for i in range(10):

    # Move forward slowly
    client.moveByVelocityAsync(2, 0, 0, 1).join()

    # Capture image
    response = client.simGetImage("0", airsim.ImageType.Scene)

    # Convert bytes to NumPy array
    img_array = np.frombuffer(response, dtype=np.uint8)

    # Decode image
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Save image
    filename = f"dataset/image_{i}.jpg"

    cv2.imwrite(filename, img)

    print("Saved", filename)

    time.sleep(1)

print("Landing...")
client.landAsync().join()

client.armDisarm(False)
client.enableApiControl(False)

print("Dataset collection completed!")
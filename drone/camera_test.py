import airsim
import cv2
import numpy as np

# Connect to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

# Capture image
response = client.simGetImage("0", airsim.ImageType.Scene)

# Convert image bytes to NumPy array
img_array = np.frombuffer(response, dtype=np.uint8)

# Decode image
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Save image
cv2.imwrite("images/drone_image.jpg", img)

print("Image saved successfully!")
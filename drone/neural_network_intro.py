import cv2
import numpy as np

# Load image
img = cv2.imread("dataset/image_0.jpg")

# Print image information
print("Image shape:", img.shape)

# Convert image into array
image_array = np.array(img)

print("\nFirst pixel value:")
print(image_array[0][0])

print("\nImage converted into numerical array successfully!")
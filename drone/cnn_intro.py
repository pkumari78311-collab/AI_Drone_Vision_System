import cv2
import numpy as np

# Load image
img = cv2.imread("dataset/image_0.jpg")

# Define a simple edge-detection kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Apply convolution
filtered = cv2.filter2D(img, -1, kernel)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("CNN-like Filter Output", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
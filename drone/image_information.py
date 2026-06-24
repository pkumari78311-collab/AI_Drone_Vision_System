import cv2

# Load image
img = cv2.imread("dataset/image_0.jpg")

# Print information
print("Shape:", img.shape)
print("Data type:", img.dtype)

# Height, Width, Channels
height, width, channels = img.shape

print("Height =", height)
print("Width =", width)
print("Channels =", channels)
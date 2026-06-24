import cv2

# Load image
img = cv2.imread("dataset/image_0.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert corner coordinates to integers
corners = corners.astype(int)

# Draw circles around detected corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 4, (0, 255, 0), -1)

# Show result
cv2.imshow("Feature Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
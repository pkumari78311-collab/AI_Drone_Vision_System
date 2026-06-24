from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    # Read frame
    success, frame = cap.read()

    if not success:
        break

    # Run YOLO detection
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLO Webcam Detection", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

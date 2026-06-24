from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Open camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame, verbose=False)

    # Get annotated frame (with boxes)
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Drone AI Vision Pipeline", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
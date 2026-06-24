from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    annotated = results[0].plot()

    # Get detected boxes
    boxes = results[0].boxes

    h, w, _ = frame.shape

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]

        # Find center of object
        cx = int((x1 + x2) / 2)

        # Decide position in frame
        if cx < w // 3:
            zone = "LEFT"
        elif cx > 2 * w // 3:
            zone = "RIGHT"
        else:
            zone = "CENTER"

        print(f"Object in: {zone}")

    cv2.imshow("Drone Navigation AI", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
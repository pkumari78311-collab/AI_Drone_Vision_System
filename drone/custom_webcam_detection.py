from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO(r"C:\Users\User\Downloads\EdgeAI_Drone_Project\runs\detect\train-3\weights\best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Custom YOLO Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
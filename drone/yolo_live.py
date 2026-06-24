from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect_and_draw(self, frame):
        results = self.model(frame)

        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                label = self.model.names[cls]

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Text label
                text = f"{label} {conf:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)

                # Position logic (left/center/right)
                center_x = (x1 + x2) / 2
                width = frame.shape[1]

                if center_x < width / 3:
                    position = "left"
                elif center_x < 2 * width / 3:
                    position = "center"
                else:
                    position = "right"

                detections.append({
                    "label": label,
                    "confidence": conf,
                    "position": position
                })

        return frame, detections
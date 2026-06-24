import cv2
from yolo_live import YOLODetector
from drone_brain import DroneBrain
from airsim_drone import AirSimDrone

detector = YOLODetector()
brain = DroneBrain()
drone = AirSimDrone()

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame, detections = detector.detect_and_draw(frame)

        if len(detections) == 0:
            action = brain.decide(None)

        else:
            best_target = brain.select_best_target(detections)
            action = brain.decide(best_target)

        drone.move(action)

        cv2.imshow("AI Drone Vision System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    drone.close()
    cap.release()
    cv2.destroyAllWindows()
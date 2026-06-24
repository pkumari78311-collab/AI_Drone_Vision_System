class DroneBrain:
    def __init__(self):
        self.locked_target = None

    def select_best_target(self, detections):
        if not detections:
            return None

        for d in detections:
            if d["label"] == "person":
                self.locked_target = "person"
                return d

        return max(detections, key=lambda x: x["confidence"])

    def decide(self, detection):

        if detection is None:
            return "SEARCH_FORWARD"

        pos = detection.get("position")

        if pos == "left":
            return "TURN_LEFT"

        elif pos == "right":
            return "TURN_RIGHT"

        elif pos == "center":
            return "MOVE_FORWARD"

        return "HOVER"
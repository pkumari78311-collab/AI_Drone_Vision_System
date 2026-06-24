from drone_brain import DroneBrain
from virtual_drone import VirtualDrone

brain = DroneBrain()
drone = VirtualDrone()

# Simulated YOLO outputs (fake input for now)
detections = [
    {"object": "box", "position": "left"},
    {"object": "box", "position": "center"},
    {"object": "box", "position": "right"},
    None
]

for d in detections:
    action = brain.decide(d)
    drone.move(action)
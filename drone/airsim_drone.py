import airsim
import time


class AirSimDrone:
    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

        self.client.enableApiControl(True)
        self.client.armDisarm(True)

        print("Taking off...")
        self.client.takeoffAsync().join()

        self.last_move = 0

    def move(self, action):

        # Allow only one movement command per second
        if time.time() - self.last_move < 1:
            return

        self.last_move = time.time()

        if action == "TURN_LEFT":
            print("AirSim: LEFT")
            self.client.moveByVelocityAsync(
                0, -1, 0, 0.5
            ).join()

        elif action == "TURN_RIGHT":
            print("AirSim: RIGHT")
            self.client.moveByVelocityAsync(
                0, 1, 0, 0.5
            ).join()

        elif action == "MOVE_FORWARD":
            print("AirSim: FORWARD")
            self.client.moveByVelocityAsync(
                1, 0, 0, 0.5
            ).join()

        elif action == "SEARCH_FORWARD":
            print("AirSim: SEARCH")
            self.client.hoverAsync().join()

        elif action == "HOVER":
            print("AirSim: HOVER")
            self.client.hoverAsync().join()

    def close(self):
        print("Landing...")
        self.client.landAsync().join()

        self.client.armDisarm(False)
        self.client.enableApiControl(False)

        print("Mission completed!")
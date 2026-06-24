class VirtualDrone:
    def move(self, action):
        if action == "TURN_LEFT":
            print("Drone turning LEFT")

        elif action == "TURN_RIGHT":
            print("Drone turning RIGHT")

        elif action == "MOVE_FORWARD":
            print("Drone moving FORWARD")

        elif action == "HOVER":
            print("Drone hovering")

        elif action == "SEARCH_FORWARD":
            print("Drone searching area")

        else:
            print("Unknown action")
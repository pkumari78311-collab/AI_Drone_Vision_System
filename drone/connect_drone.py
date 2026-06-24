import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()

client.enableApiControl(True)
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

time.sleep(2)

print("Moving forward...")
client.moveByVelocityAsync(3, 0, 0, 5).join()

time.sleep(1)

print("Moving right...")
client.moveByVelocityAsync(0, 3, 0, 3).join()

time.sleep(1)

print("Landing...")
client.landAsync().join()

client.armDisarm(False)
client.enableApiControl(False)

print("Mission completed!")
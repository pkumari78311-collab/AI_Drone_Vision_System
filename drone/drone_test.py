import airsim
import time

# Connect to AirSim
client = airsim.MultirotorClient()
client.confirmConnection()

# Enable control
client.enableApiControl(True)
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

# Rise up
client.moveByVelocityAsync(0, 0, -3, 5).join()

# Move forward
client.moveByVelocityAsync(5, 0, 0, 5).join()

# Move right
client.moveByVelocityAsync(0, 5, 0, 5).join()

# Rotate slowly
client.rotateByYawRateAsync(20, 9).join()

# Hover for observation
client.hoverAsync().join()
time.sleep(5)

print("Landing...")
client.landAsync().join()

# Release control
client.armDisarm(False)
client.enableApiControl(False)

print("Mission completed!")
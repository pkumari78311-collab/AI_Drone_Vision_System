frame_width = 640

# Example detected object center
object_center_x = 500

# Decide movement

if object_center_x < frame_width/3:
    print("MOVE LEFT")

elif object_center_x < 2*frame_width/3:
    print("MOVE FORWARD")

else:
    print("MOVE RIGHT")
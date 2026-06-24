frame_width = 640

# Assume YOLO detected an object whose center is at x=500
object_center_x = 500

if object_center_x < frame_width/3:
    command = "MOVE LEFT"

elif object_center_x < 2*frame_width/3:
    command = "MOVE FORWARD"

else:
    command = "MOVE RIGHT"

print(command)
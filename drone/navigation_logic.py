# Frame width
frame_width = 640

# Example object center position
object_center_x = 150

# Navigation decision

if object_center_x < frame_width/3:
    print("LEFT")

elif object_center_x < 2*frame_width/3:
    print("CENTER")

else:
    print("RIGHT")
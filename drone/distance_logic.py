# Example object width in pixels
object_width = 250

# Distance estimation

if object_width > 300:
    print("TOO CLOSE")

elif object_width > 150:
    print("CAUTION")

else:
    print("SAFE DISTANCE")
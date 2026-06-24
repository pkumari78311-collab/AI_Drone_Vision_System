import cv2

image_path = r"C:\Users\User\Downloads\EdgeAI_Drone_Project\images\car.jpg"

img = cv2.imread(image_path)

if img is None:
    print("OpenCV cannot read the image.")
else:
    print("OpenCV loaded the image successfully.")
    print("Image shape:", img.shape)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2

cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    cv2.imwrite("AdMub/admub.jpg", frame)
    print("Image saved.")
else:
    print("Failed to capture.")

cam.release()

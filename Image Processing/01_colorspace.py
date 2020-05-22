import cv2
import numpy as np

# List all the available flags for color conversion
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print("Possible Color conversions:\n", flags)

# Object Tracking only blue color objects
cap = cv2.VideoCapture("../Media Files/input_videos/vid_2.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(src=hsv, lowerb=lower_blue, upperb=upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(src1=frame, src2=frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Masked', mask)
    cv2.imshow('Result', res)

    # To view frame by frame
    if cv2.waitKey(200) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

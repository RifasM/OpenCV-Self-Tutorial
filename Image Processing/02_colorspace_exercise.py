import numpy as np
import cv2

cap = cv2.VideoCapture("../Media Files/input_videos/vid_2.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # converting to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower and upper bound values
    # red
    lower_red = np.array([60, 50, 100])
    upper_red = np.array([255, 255, 130])

    # blue
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # green
    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255])

    # Generate masks
    mask_blue = cv2.inRange(src=hsv, lowerb=lower_blue, upperb=upper_blue)
    mask_green = cv2.inRange(src=hsv, lowerb=lower_green, upperb=upper_green)
    mask_red = cv2.inRange(src=hsv, lowerb=lower_red, upperb=upper_red)

    # Bitwise and the masks with the image
    res = cv2.bitwise_and(src1=frame, src2=frame, mask=mask_blue+mask_green+mask_red)

    cv2.imshow('Original', frame)
    cv2.imshow('Masked Red', mask_red)
    cv2.imshow('Masked Green', mask_green)
    cv2.imshow('Masked Blue', mask_blue)
    cv2.imshow('Result', res)

    if cv2.waitKey(200) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np


def nothing(x):
    pass


# Create a black Track bar, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Track bar')

# create track bars for color change
# cv2.createTrackbar(trackBarName, windowName, value, count, callback (onChange))
cv2.createTrackbar('R', "Track bar", 0, 255, nothing)
cv2.createTrackbar('G', 'Track bar', 0, 255, nothing)
cv2.createTrackbar('B', 'Track bar', 0, 255, nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF 1 : ON'
cv2.createTrackbar(switch, 'Track bar', 0, 1, nothing)

while True:
    cv2.imshow('Track bar', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four track bars
    r = cv2.getTrackbarPos('R', 'Track bar')
    g = cv2.getTrackbarPos('G', 'Track bar')
    b = cv2.getTrackbarPos('B', 'Track bar')
    s = cv2.getTrackbarPos(switch, 'Track bar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()

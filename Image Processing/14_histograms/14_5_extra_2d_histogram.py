import cv2
import numpy as np


# built-in modules


def set_scale(val):
    global hist_scale
    hist_scale = val


hsv_map = np.zeros((180, 256, 3), np.uint8)
h, s = np.indices(hsv_map.shape[:2])
hsv_map[:, :, 0] = h
hsv_map[:, :, 1] = s
hsv_map[:, :, 2] = 255
hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
cv2.imshow('hsv_map', hsv_map)

cv2.namedWindow('hist', 0)
hist_scale = 10

cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

cap = cv2.VideoCapture(0)

while True:
    _flag, frame = cap.read()
    cv2.imshow('camera', frame)

    small = cv2.pyrDown(frame)

    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    dark = hsv[..., 2] < 32
    hsv[dark] = 0
    h = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    h = np.clip(h * 0.005 * hist_scale, 0, 1)
    vis = hsv_map * h[:, :, np.newaxis] / 255.0
    cv2.imshow('hist', vis)

    ch = cv2.waitKey(1)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()

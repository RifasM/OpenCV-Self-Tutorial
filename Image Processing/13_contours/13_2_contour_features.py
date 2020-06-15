import cv2
import numpy as np

img = cv2.imread('../../Media Files/input_images/img_16.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(array=cnt)
print("Moments:\n", M)

"""
From this moments, you can extract useful data like area, centroid etc. 
Centroid is given by the relations, 
C_x = frac{M_{10}}{M_{00}} 
and
C_y = frac{M_{01}}{M_{00}}
"""
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print("Centroid: (", cx, ", ", cy, ")")

import cv2
import numpy as np

img = cv2.imread('../../Media Files/input_images/img_17.jpg', 0)
img_copy = img.copy()
cv2.imshow("Original Image", img)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
img_copy = cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)
cv2.imshow("All Contours", img_copy)
del img_copy

cnt = contours[0]
img_copy = img.copy()
img_copy = cv2.drawContours(img_copy, [cnt], 0, (255, 0, 0), 5)
cv2.imshow("1st Contour", img_copy)
M = cv2.moments(array=cnt)
print("Moments of 1st Contour:\n", M)

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

# Contour Area is given by M00
area = cv2.contourArea(cnt)
print("Area:", area)

# Perimeter
"""
It is also called arc length. 
It can be found out using cv2.arcLength() function. 
Second argument specify whether shape is a closed contour (True = closed contour), or just a curve.
"""
perimeter = cv2.arcLength(cnt, True)
print("Arc Length (Perimeter):", perimeter)

cv2.waitKey(0)
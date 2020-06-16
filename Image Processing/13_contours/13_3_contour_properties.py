import cv2
import numpy as np

img = cv2.imread('../../Media Files/input_images/img_19.jpg')
col_img = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", img)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
img_copy = cv2.drawContours(col_img.copy(), contours, -1, (0, 255, 0), 2)
cv2.imshow("All Contours", img_copy)

cnt = contours[0]

# Aspect Ratio
# It is the ratio of width to height of bounding rect of the object.
x, y, w, h = cv2.boundingRect(array=cnt)
aspect_ratio = float(w) / h
print("Aspect Ratio:", aspect_ratio)

# Extent
# Extent is the ratio of contour area to bounding rectangle area.
area = cv2.contourArea(contour=cnt)
print("Contour Area:", area)
rect_area = w*h
print("Rectangle Area:", rect_area)
extent = float(area)/rect_area
print("Extent:", extent)

# Solidity
# Solidity is the ratio of contour area to its convex hull area.
hull = cv2.convexHull(cnt)
img_copy = cv2.drawContours(col_img.copy(), hull, -1, (255, 0, 0), 3)
cv2.imshow("Convex Hull", img_copy)
hull_area = cv2.contourArea(hull)
print("Hull Area:", hull_area)
solidity = float(area)/hull_area
print("Solidity:", solidity)

cv2.waitKey(0)
cv2.destroyAllWindows()

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
img_copy = cv2.rectangle(col_img.copy(), (x, y), (x + w, y + h), (0, 255, 255), 3)
aspect_ratio = float(w) / h
print("Aspect Ratio:", aspect_ratio)

# Extent
# Extent is the ratio of contour area to bounding rectangle area.
area = cv2.contourArea(contour=cnt)
print("Contour Area:", area)
rect_area = w * h
print("Rectangle Area:", rect_area)
extent = float(area) / rect_area
print("Extent:", extent)

# Solidity
# Solidity is the ratio of contour area to its convex hull area.
hull = cv2.convexHull(cnt)
img_copy = cv2.drawContours(img_copy, hull, -1, (255, 0, 0), 7)
img_copy = cv2.polylines(img_copy, [hull], True, (255, 255, 0), 2)
cv2.imshow("Convex Hull(Blue) and Bounding Box(Yellow)", img_copy)
hull_area = cv2.contourArea(hull)
print("Hull Area:", hull_area)
solidity = float(area) / hull_area
print("Solidity:", solidity)

# Equivalent Diameter
# Equivalent Diameter is the diameter of the circle whose area is same as the contour area.
equi_diameter = np.sqrt(4 * area / np.pi)
print("Equivalent Diameter:", equi_diameter)

# Orientation
# Orientation is the angle at which object is directed.
# Following method also gives the Major Axis and Minor Axis lengths.
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print("Orientation\n\t(x, y): (", x, ",", y, ")\n\tMajor Axis:", MA, "\n\tMinor Axis:", ma)

# Masks and Pixel Points
mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
print("Pixel Points using Numpy:\n", pixelpoints)
pixelpoints = cv2.findNonZero(mask)
print("Pixel Points using CV2:\n", pixelpoints)
"""
Here, two methods, one using Numpy functions, next one using OpenCV function 
(last commented line) are given to do the same. Results are also same, 
but with a slight difference. 
Numpy gives coordinates in (row, column) format, while 
OpenCV gives coordinates in (x,y) format. 
So basically the answers will be interchanged. 
Note that, row = x and column = y.
"""

# Maximum and Minimum Values
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(src=img, mask=mask)
print("Mask Values\n\tMinimum Value:", min_val, "\n\tMinimum Value Location:",
      min_loc, "\n\tMaximum Value:", max_val, "\n\tMaximum Value Location:", max_loc)

# Mean Color or Intensity
# We can find the average color of an object.
# Or it can be average intensity of the object in grayscale mode.
mean_val = cv2.mean(src=img, mask=mask)
print("Mean Value:", mean_val)

# Extreme Points
# Extreme Points means topmost, bottommost, rightmost and leftmost points of the object.
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print("Extreme Points:\n\tLeftmost:", leftmost, "\n\tRightMost:", rightmost, "\n\tTopMost:",
      topmost, "\n\tBottomMost:", bottommost)
cv2.circle(col_img, leftmost, 7, (255, 200, 0), -1)
cv2.circle(col_img, rightmost, 7, (255, 200, 0), -1)
cv2.circle(col_img, topmost, 7, (255, 200, 0), -1)
cv2.circle(col_img, bottommost, 7, (255, 200, 0), -1)
cv2.imshow("Extreme Points", col_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

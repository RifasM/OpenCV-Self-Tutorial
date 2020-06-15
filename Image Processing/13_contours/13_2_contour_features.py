import cv2
import numpy as np

img = cv2.imread('../../Media Files/input_images/img_17.jpg')
col_img = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", img)
ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
img_copy = cv2.drawContours(col_img.copy(), contours, -1, (0, 255, 0), 2)
cv2.imshow("All Contours", img_copy)

cnt = contours[0]
img_copy = cv2.drawContours(col_img.copy(), [cnt], 0, (255, 0, 0), 2)
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
perimeter = cv2.arcLength(curve=cnt, closed=True)
print("Arc Length (Perimeter):", perimeter)

# Contour Approximation
epsilon_1 = 0.01 * perimeter
epsilon_10 = 0.1 * perimeter

approx_1 = cv2.approxPolyDP(curve=cnt, epsilon=epsilon_1, closed=True)
approx_1 = cv2.drawContours(col_img.copy(), [approx_1], -1, (0, 255, 200), 2)
cv2.imshow("Approximation 1%", approx_1)

approx_10 = cv2.approxPolyDP(curve=cnt, epsilon=epsilon_10, closed=True)
approx_10 = cv2.drawContours(col_img.copy(), [approx_10], -1, (0, 0, 255), 2)
cv2.imshow("Approximation 10%", approx_10)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Convex Hull
"""
SYNTAX: 
 hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]
     - points are the contours we pass into.
     - hull is the output, normally we avoid it.
     - clockwise : Orientation flag. 
                   If it is True, the output convex hull is oriented clockwise. 
                   Otherwise, it is oriented counter-clockwise.
     - returnPoints : By default, True. 
                      Then it returns the coordinates of the hull points. 
                      If False, it returns the indices of contour points corresponding to the hull points.
"""
img = cv2.imread('../../Media Files/input_images/img_16.jpg')
col_img = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", col_img)
_, thresh = cv2.threshold(img, 127, 255, 0)
contours, _ = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

hull = cv2.convexHull(points=cnt)  # returnPoints = True (default)
print("Default Hull:\n", hull)
hull = cv2.drawContours(col_img.copy(), hull, -1, (0, 127, 127), 5)
cv2.imshow("Default Hull (Return Points True)", hull)

hull = cv2.convexHull(points=cnt, returnPoints=False)
print("Return Points False Hull:\n", hull)
# These are the indices of corresponding points in contours

imcopy = col_img.copy()
hull_img = np.ones_like(img)
for i in hull:
    hull_img = cv2.drawContours(imcopy, contours[0], i, (0, 127, 127), 5)
cv2.imshow("Return Points False Hull", hull_img)

k = cv2.isContourConvex(cnt)
print("Is Contour Convex?", k)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Bounding Rectangle
img = cv2.imread('../../Media Files/input_images/img_18.jpg')
col_img = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", col_img)
_, thresh = cv2.threshold(img, 127, 255, 0)
contours, _ = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

# Straight Bounding Rectangle
x, y, w, h = cv2.boundingRect(array=cnt)
img_copy = cv2.rectangle(img=col_img.copy(), pt1=(int(x), int(y)), pt2=(int(x + w), int(y + h)), color=(255, 0, 0),
                         thickness=2)
cv2.imshow("Normal Bounding rectangle", img_copy)

# Rotated Rectangle
rect = cv2.minAreaRect(points=cnt)
box = cv2.boxPoints(box=rect)
box = np.int0(box)
img_copy = cv2.drawContours(col_img.copy(), [box], 0, (0, 0, 255), 2)
cv2.imshow("Rotated Bounding rectangle", img_copy)

# Minimum Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(points=cnt)
center = (int(x), int(y))
img_copy = cv2.circle(img=col_img.copy(), center=center, radius=int(radius), color=(0, 255, 0), thickness=2)
cv2.imshow("Minimum Enclosing Circle", img_copy)

# Ellipse
ellipse = cv2.fitEllipse(points=cnt)
img_copy = cv2.ellipse(img=col_img.copy(), box=ellipse, color=(0, 255, 0), thickness=2)
cv2.imshow("Ellipse", img_copy)

# Line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(points=cnt, distType=cv2.DIST_L2, param=0, reps=0.01, aeps=0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
img_copy = cv2.line(img=col_img.copy(), pt1=(cols - 1, righty), pt2=(0, lefty), color=(0, 255, 0), thickness=2)
cv2.imshow("Line", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()

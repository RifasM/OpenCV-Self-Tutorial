import re

import cv2
import numpy as np

img = cv2.imread('../../Media Files/input_images/img_17.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt = contours[0]

# Convexity Defects
hull = cv2.convexHull(cnt, returnPoints=False)
# Remember we have to pass
# returnPoints = False
# while finding convex hull, in order to find convexity defects.
defects = cv2.convexityDefects(contour=cnt, convexhull=hull)
print("Defects\n", defects)
"""
It returns an array where each row contains these values - 
[ start point, end point, farthest point, approximate distance to farthest point ]. 

We draw a line joining start point and end point, then draw a circle at the farthest point. 
Remember first three values returned are indices of cnt. So we have to bring those values from cnt.
"""

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Point Polygon Test
"""
This function finds the shortest distance between a point in the image and a contour. 
It returns the distance which is negative when point is outside the contour, positive 
when point is inside and zero if point is on the contour.
"""
dist = cv2.pointPolygonTest(contour=cnt, pt=(50, 50), measureDist=True)
# If you don’t want to find the distance, make sure third argument is False,
# because, it is a time consuming process.
# So, making it False gives about 2-3X speedup.
print("Distance of point (50, 50) in contour :", dist)
if dist == 0:
    point = "On the contour"
elif dist == -1:
    point = "Outside the contour"
else:
    point = "Inside the contour"
print("Where is the point (50, 50)?: ", point)

# Match Shapes
"""
cv2.matchShapes() which enables us to compare two shapes, or two contours and returns a 
metric showing the similarity. 
The lower the result, the better match it is. 
It is calculated based on the hu-moment values.

Hu-Moments are seven moments invariant to translation, rotation and scale. 
Seventh one is skew-invariant. Those values can be found using cv2.HuMoments() function.
"""
img1 = cv2.imread('../../Media Files/input_images/img_17.jpg', 0)
img2 = cv2.imread('../../Media Files/input_images/img_13.jpg', 0)

_, thresh = cv2.threshold(img1, 127, 255, 0)
_, thresh2 = cv2.threshold(img2, 127, 255, 0)
contours, _ = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, _ = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(contour1=cnt1, contour2=cnt2, method=cv2.CONTOURS_MATCH_I1, parameter=0.0)
print("Shapes Matched?:", ret)

[print(d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(CONTOURS_MATCH_).*', i)]]

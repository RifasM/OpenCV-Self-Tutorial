import cv2
import numpy as np
import re

print("Available modes for contour: ")
[print("\t", d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(RETR_).*', i)]]

print("\nAvailable methods for contour: ")
[print("\t", d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(CHAIN_).*', i)]]

img = cv2.imread('../../Media Files/input_images/img_3.jpg')
col_img = img

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)

"""
So each contour has its own information regarding what hierarchy it is, 
who is its child, who is its parent etc. 
OpenCV represents it as an array of four values : 
[Next, Previous, First_Child, Parent]

- Next denotes next contour at the same hierarchical level.
- Previous denotes previous contour at the same hierarchical level.
- First_Child denotes its first child contour.
- Parent denotes index of its parent contour.

If there is no child or parent, that field is taken as -1
If there are no values, it is set to -1

Refer:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_hierarchy/py_contours_hierarchy.html#hierarchy-representation-in-opencv
"""

#  Retrieval Modes
# RETR_LIST
"""
 It simply retrieves all the contours, but doesn’t create any parent-child relationship. 
 Parents and kids are equal under this rule, and they are just contours. ie they all belongs to same hierarchy level.
 This is the good choice to use in your code, if you are not using any hierarchy features.
"""
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
print("\nHierarchy for RETR_LIST:\n", hierarchy)
img_copy = cv2.drawContours(col_img.copy(), contours, -1, (255, 200, 200), 2)
cv2.imshow("RETR_LIST", img_copy)
cv2.waitKey(0)

# RETR_EXTERNAL
"""
 it returns only extreme outer flags. All child contours are left behind. 
 We can say, under this law, Only the eldest in every family is taken care of. 
 It doesn’t care about other members of the family
"""
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
print("\nHierarchy for RETR_EXTERNAL:\n", hierarchy)
img_copy = cv2.drawContours(col_img.copy(), contours, -1, (255, 200, 200), 2)
cv2.imshow("RETR_EXTERNAL", img_copy)
cv2.waitKey(0)

# RETR_CCOMP
"""
This flag retrieves all the contours and arranges them to a 2-level hierarchy. 
ie external contours of the object (ie its boundary) are placed in hierarchy-1. 
And the contours of holes inside object (if any) is placed in hierarchy-2. 
If any object inside it, its contour is placed again in hierarchy-1 only. 
And its hole in hierarchy-2 and so on.
"""
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_NONE)
print("\nHierarchy for RETR_CCOMP:\n", hierarchy)
img_copy = cv2.drawContours(col_img.copy(), contours, -1, (255, 200, 200), 2)
cv2.imshow("RETR_CCOMP", img_copy)
cv2.waitKey(0)

# RETR_TREE
"""
It retrieves all the contours and creates a full family hierarchy list. 
It even tells, who is the grandpa, father, son, grandson and even beyond...
"""
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
print("\nHierarchy for RETR_TREE:\n", hierarchy)
img_copy = cv2.drawContours(col_img.copy(), contours, -1, (255, 200, 200), 2)
cv2.imshow("RETR_TREE", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

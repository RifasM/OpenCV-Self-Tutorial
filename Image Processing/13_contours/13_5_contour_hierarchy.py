import cv2
import numpy as np
import re

print("Available modes for contour: ")
[print("\t", d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(RETR_).*', i)]]

print("\nAvailable methods for contour: ")
[print("\t", d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(CHAIN_).*', i)]]

img = cv2.imread('../../Media Files/input_images/img_3.jpg')

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

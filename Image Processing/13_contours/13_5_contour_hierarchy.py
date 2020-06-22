import cv2
import numpy as np

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
"""
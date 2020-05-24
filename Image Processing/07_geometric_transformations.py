import cv2
import numpy as np

# cv2.warpAffine takes a 2x3 transformation matrix while
# cv2.warpPerspective takes a 3x3 transformation matrix as input.

# SCALING
# Preferable interpolation methods are cv2.INTER_AREA for shrinking and
# cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. By default,
# interpolation method used is cv2.INTER_LINEAR for all resizing purposes
img = cv2.imread('../Media Files/input_images/img_2.jpg')

res = cv2.resize(src=img, dsize=None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Result 1", res)

height, width = img.shape[:2]
res = cv2.resize(src=img, dsize=(2 * width, 2 * height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Result 2", res)

cv2.waitKey(0)

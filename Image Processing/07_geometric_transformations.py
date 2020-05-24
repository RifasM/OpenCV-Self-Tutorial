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

cv2.imshow("Scaling Result 1", res)

height, width = img.shape[:2]
res = cv2.resize(src=img, dsize=(2 * width, 2 * height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Scaling Result 2", res)

cv2.waitKey(0)
cv2.destroyAllWindows()

# TRANSLATION
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = img.shape

# shift of (100, 50) -> (cols to shift, rows to shift)
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(src=img, M=M, dsize=(cols, rows))

cv2.imshow('Translation Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ROTATION

# rotates the image by 90 degree with respect to center without any scaling
M = cv2.getRotationMatrix2D(center=(cols / 2, rows / 2), angle=90, scale=1)
dst = cv2.warpAffine(src=img, M=M, dsize=(cols, rows))

cv2.imshow('Rotation Result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


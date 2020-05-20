import cv2
import numpy as np

# Basics operations
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))                                                # 250+10 = 260 => 255
print(x + y)                                                        # 250+10 = 260 % 256 = 4

# Image Blending
# This is also image addition, but different weights are given to images
# so that it gives a feeling of blending or transparency.
img1 = cv2.imread('../Media Files/input_images/img_2.jpg')
img2 = cv2.imread('../Media Files/input_images/img_3.jpg')

# To make sure both the images are of the same size
img1 = cv2.resize(img1, dsize=(174, 179), interpolation=cv2.INTER_CUBIC)
img2 = cv2.resize(img2, dsize=(174, 179), interpolation=cv2.INTER_CUBIC)

# First image is given a weight of 0.7 and second image is given 0.3, gamma is taken as 0
dst = cv2.addWeighted(src1=img1, alpha=0.7, src2=img2, beta=0.3, gamma=2)

cv2.imshow('Added', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Media Files/input_images/img_3.jpg')

# 2D Convolution ( Image Filtering )
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# Image Blurring (Image Smoothing)
# 1. Averaging
"""
This is done by convolving the image with a normalized box filter.
It simply takes the average of all the pixels under kernel area 
and replaces the central element with this average. 
This is done by the function cv2.blur() or cv2.boxFilter().

If you don’t want to use a normalized box filter, 
use cv2.boxFilter() and pass the argument normalize=False to the function.
"""
blur = cv2.blur(src=img, ksize=(5, 5))
boxFilterFalse = cv2.boxFilter(src=img, ddepth=0, ksize=(5, 5), normalize=False)
boxFilterTrue = cv2.boxFilter(src=img, ddepth=0, ksize=(5, 5), normalize=True)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(boxFilterFalse), plt.title('Box Filter False')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(boxFilterTrue), plt.title('Box Filter True')
plt.xticks([]), plt.yticks([])
plt.show()

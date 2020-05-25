import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Media Files/input_images/img_10.jpg')

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

# 2. Gaussian Filtering
"""
We should specify the width and height of the kernel which should be positive and odd.
We also should specify the standard deviation in the X and Y directions, sigmaX and 
sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX. 

If both are given as zeros, they are calculated from the kernel size. 
Gaussian filtering is highly effective in removing Gaussian noise from the image.
"""
blur = cv2.GaussianBlur(src=img, ksize=(5, 5), sigmaX=0)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# Using Gaussian Kernel
kernel = cv2.getGaussianKernel(ksize=5, sigma=0)
print(kernel)
dst = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
plt.imshow(dst), plt.title("kernel")
plt.show()

# 3. Median Filtering
"""
the function cv2.medianBlur() computes the median of all the pixels 
under the kernel window and the central pixel is replaced with this median value. 
"""
median = cv2.medianBlur(src=img, ksize=5)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(median), plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

# 4. Bilateral Filtering
"""
cv2.bilateralFilter(), which was defined for, and is highly effective at noise removal 
while preserving edges. But the operation is slower compared to other filters.
This Gaussian filter is a function of space alone, that is, nearby pixels are considered 
while filtering. It does not consider whether pixels have almost the same intensity 
value and does not consider whether the pixel lies on an edge or not. 
The resulting effect is that Gaussian filters tend to blur edges, which is undesirable.
"""
blur = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Bilateral Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

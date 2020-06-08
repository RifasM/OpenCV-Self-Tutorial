import cv2
import numpy as np
import re
import matplotlib.pyplot as plt

"""
OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr and Laplacian.

- Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. 
- You can also specify the size of kernel by the argument ksize. 
  If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter.
- Laplacian Derivative calculates the Laplacian of the image given by the relation, 
  \Delta src = \frac{\partial ^2{src}}{\partial x^2} + \frac{\partial ^2{src}}{\partial y^2}
"""

img = cv2.imread('../Media Files/input_images/img_12.jpg', 0)

# Print all available ddtypes
# ninghang.blogspot.com/2012/11/list-of-mat-type-in-opencv.html
# https://docs.opencv.org/2.4/modules/core/doc/basic_structures.html#mat-depth
[print(d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(CV_).*', i)]]
"""
Number is how many bytes the matrix values have.
U symbol marks unsigned int.
F marks floating point
Therefore:
8U is equivalent of unsigned char
32F is equivalent of float
64F is equivalent of double

C1, C2, C3 mean, how many Channels each value has.
"""

# All kernels are of 5x5 size. Depth of output image is passed -1 to get the result in np.uint8 type.

laplacian = cv2.Laplacian(src=img, ddepth=cv2.CV_8U, ksize=5)

sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_8U, dx=0, dy=1, ksize=5)

scharrx = cv2.Scharr(src=img, ddepth=cv2.CV_8U, dx=1, dy=0)
scharry = cv2.Scharr(src=img, ddepth=cv2.CV_8U, dx=0, dy=1)

plt.subplot(3, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 5), plt.imshow(scharrx, cmap='gray')
plt.title('Scharr X'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 6), plt.imshow(scharry, cmap='gray')
plt.title('Scharr Y'), plt.xticks([]), plt.yticks([])

plt.show()

img = cv2.imread('../Media Files/input_images/img_13.jpg', 0)

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(src=img, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=5)

# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()

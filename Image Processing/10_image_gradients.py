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
[print(d, ":", getattr(cv2, d)) for d in [i for i in dir(cv2) if re.match('^(CV_).*', i)]]

laplacian = cv2.Laplacian(src=img, ddepth=cv2.CV_64F, ksize=5)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()

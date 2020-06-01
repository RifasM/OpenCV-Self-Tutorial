import cv2
import numpy as np

"""
Morphological transformations are some simple operations based on the image shape. 
It is normally performed on binary images. It needs two inputs, one is our original image, 
second one is called structuring element or kernel which decides the nature of operation. 
Two basic morphological operators are Erosion and Dilation. 
Then its variant forms like Opening, Closing, Gradient etc also comes into play. 
"""
img = cv2.imread('../Media Files/input_images/img_11.jpg', 0)
cv2.imshow("Original", img)

# EROSION
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)

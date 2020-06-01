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
"""
The basic idea of erosion is just like soil erosion only, 
it erodes away the boundaries of foreground object
A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels 
under the kernel is 1, otherwise it is eroded (made to zero).

So what happens is that, all the pixels near boundary will be discarded depending upon 
the size of kernel. 
So the thickness or size of the foreground object decreases or simply white region 
decreases in the image. 
"""
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)

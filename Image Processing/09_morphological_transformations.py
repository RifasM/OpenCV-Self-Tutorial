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
kernel = np.ones((5, 5), np.uint8)
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
erosion = cv2.erode(src=img, kernel=kernel, iterations=1)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)

# Dilation
"""
Here, a pixel element is ‘1’ if at least one pixel under the kernel is ‘1’. 
So it increases the white region in the image or size of foreground object increases. 
Normally, in cases like noise removal, erosion is followed by dilation. 
Because, erosion removes white noises, but it also shrinks our object. 
So we dilate it. Since noise is gone, they won’t come back, but our object area increases. 
It is also useful in joining broken parts of an object.
"""
dilation = cv2.dilate(src=img, kernel=kernel, iterations=1)
erosion_dilation = cv2.dilate(src=img, kernel=kernel, iterations=1)
cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion followed by Dilation", erosion_dilation)

cv2.waitKey(0)

# OPENING
"""
Opening is just another name of erosion followed by dilation. It is useful in removing noise
"""
opening = cv2.morphologyEx(src=img, op=cv2.MORPH_OPEN, kernel=kernel)
cv2.imshow("Opening", opening)

cv2.waitKey(0)

# CLOSING
"""
Closing is reverse of Opening, Dilation followed by Erosion. 
It is useful in closing small holes inside the foreground objects, or small black points on the object.
"""
closing = cv2.morphologyEx(src=img, op=cv2.MORPH_CLOSE, kernel=kernel)
cv2.imshow("Closing", closing)

cv2.waitKey(0)

# MORPHOLOGICAL GRADIENT
gradient = cv2.morphologyEx(src=img, op=cv2.MORPH_GRADIENT, kernel=kernel)
cv2.imshow("Gradient", gradient)

cv2.waitKey(0)

# TOP HAT
top_hat = cv2.morphologyEx(src=img, op=cv2.MORPH_TOPHAT, kernel=kernel)
cv2.imshow("Top Hat", top_hat)

cv2.waitKey(0)

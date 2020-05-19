import cv2
import numpy as np

img = cv2.imread('../Media Files/input_images/img_1.jpg')

print("Image Properties: ", img.shape)
# It returns a tuple of number of rows, columns and channels (if image is color)
# If image is grayscale, tuple returned contains only number of rows and columns.
# So it is a good method to check if loaded image is grayscale or color image.

print("Image Height: ", img.shape[0])
print("Image Width: ", img.shape[1])
print("Image Channels: ", img.shape[2])

print("Number of pixels: ", img.size)         # Total number of pixels

print("Datatype of image: ", img.dtype)        # Image datatype
# img.dtype is very important while debugging because a large number of errors
# in OpenCV-Python code is caused by invalid datatype.

import cv2
import numpy as np

# You can access a pixel value by its row and column coordinates.
# For BGR image, it returns an array of Blue, Green, Red values
img = cv2.imread('../Media Files/input_images/img_1.jpg')
px = img[100, 100]                                              # accessing pixel values at (100, 100)
print("Initial: ", px)

blue = img[100, 100, 0]                                         # accessing only blue pixel at (100, 100)
green = img[100, 100, 1]                                        # accessing only green pixel at (100, 100)
red = img[100, 100, 2]                                          # accessing only red pixel at (100, 100)
print("Blue: ", blue)
print("Green: ", green)
print("Red: ", red)

img[100, 100] = [255, 255, 255]                                  # Changing pixel Value at (100, 100)
print("Changed: ", img[100, 100])

# Better pixel accessing and editing method


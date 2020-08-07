import cv2
import matplotlib.pyplot as plt

"""
There are two ways for this,
Short Way : use Matplotlib plotting functions
Long Way : use OpenCV drawing functions
"""

# Using Matplotlib
img = cv2.imread('../../Media Files/input_images/img_5.jpg', 0)
plt.hist(x=img.ravel(), bins=256, range=[0, 256])
plt.title("Matplotlib Histogram")
plt.show()

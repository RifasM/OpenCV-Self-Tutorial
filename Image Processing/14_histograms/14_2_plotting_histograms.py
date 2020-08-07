import cv2
import matplotlib.pyplot as plt

"""
There are two ways for this,
Short Way : use Matplotlib plotting functions
Long Way : use OpenCV drawing functions
"""

# Using Matplotlib
img = cv2.imread('../../Media Files/input_images/img_5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.hist(x=grey_img.ravel(), bins=256, range=[0, 256])
plt.title("Matplotlib Histogram")
plt.show()

# OR

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title("BGP Histogram Plot")
plt.show()

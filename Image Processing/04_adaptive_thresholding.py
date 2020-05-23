import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Media Files/input_images/img_5.jpg', 0)
img = cv2.medianBlur(src=img, ksize=5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# the algorithm calculate the threshold for a small regions of the image.
# So we get different thresholds for different regions of the same image
# and it gives us better results for images with varying illumination.

"""
v2.ADAPTIVE_THRESH_MEAN_C: 
Threshold Value = (Mean of the neighbourhood area values – constant value). 
In other words, it is the mean of the blockSize×blockSize neighborhood of a point minus constant.

cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 
Threshold Value = (Gaussian-weighted sum of the neighbourhood values – constant value).
In other words, it is a weighted sum of the blockSize×blockSize neighborhood of a point minus constant.
"""
th2 = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                            thresholdType=cv2.THRESH_BINARY, blockSize=11, C=2)
th3 = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            thresholdType=cv2.THRESH_BINARY, blockSize=11, C=2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
STEPS
- Noise Reduction
- Finding Intensity Gradient
- Non-maximum Suppression
- Hysteresis Thresholding
"""

img = cv2.imread('../Media Files/input_images/img_2.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

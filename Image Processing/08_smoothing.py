import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Media Files/input_images/img_3.jpg')

# 2D Convolution ( Image Filtering )
kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [0, 0, 255]

img1 = cv2.imread('../Media Files/input_images/img_3.jpg')

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#making-borders-for-images-padding

replicate = cv2.copyMakeBorder(src=img1, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(src=img1, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(src=img1, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(src=img1, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(src=img1, top=10, bottom=10, left=10, right=10, borderType=cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()

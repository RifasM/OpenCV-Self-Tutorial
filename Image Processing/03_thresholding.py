import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../Media Files/input_images/img_6.jpg', 0)
_, thresh1 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
_, thresh3 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TRUNC)
_, thresh4 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)
_, thresh5 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

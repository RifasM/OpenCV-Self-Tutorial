import numpy as np
import cv2

img = cv2.imread('../../Media Files/input_images/img_3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=0)
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
# First one is source image, second is contour retrieval mode, third is contour approximation method

# Draw All contours
img_all = cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3)
cv2.imshow("Image with all contours", img_all)
cv2.waitKey(0)

# Draw 2nd contour
img_2 = cv2.drawContours(image=img, contours=contours, contourIdx=1, color=(0, 255, 0), thickness=3)
cv2.imshow("Image with 2nd contour", img_2)
cv2.waitKey(0)


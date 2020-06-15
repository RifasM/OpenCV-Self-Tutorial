import numpy as np
import cv2

img = cv2.imread('../../Media Files/input_images/img_4.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=0)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
# First one is source image, second is contour retrieval mode, third is contour approximation method

img_copy = img.copy()
# Draw All contours
img = cv2.drawContours(image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=3)
cv2.imshow("Image with all contours", img)
cv2.waitKey(0)

img_copy1 = img_copy.copy()
# Draw 2nd contour
img_copy = cv2.drawContours(image=img_copy, contours=contours, contourIdx=1, color=(0, 255, 0), thickness=3)
cv2.imshow("Image with 2nd contour method 1", img_copy)
cv2.waitKey(0)
# or
cnt = contours[4]
img_copy2 = img_copy1.copy()
img_copy1 = cv2.drawContours(image=img_copy1, contours=[cnt], contourIdx=0, color=(0, 255, 0), thickness=3)
cv2.imshow("Image with 2nd contour method 2", img_copy1)
cv2.waitKey(0)

cv2.destroyAllWindows()

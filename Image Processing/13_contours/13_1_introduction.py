import numpy as np
import cv2

img = cv2.imread('../../Media Files/input_images/img_2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(src=img_gray, thresh=127, maxval=255, type=0)
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

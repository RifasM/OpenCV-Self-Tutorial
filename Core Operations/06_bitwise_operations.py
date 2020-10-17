import cv2
import numpy as np

# Load two images
img1 = cv2.imread('../Media Files/input_images/img_2.jpg')
img2 = cv2.imread('../Media Files/input_images/img_3.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(src=img2gray, thresh=10, maxval=255, type=cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

# Show all the images
cv2.imshow("Grey", img2gray)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Inverse", mask_inv)
cv2.imshow("Background", img1_bg)
cv2.imshow("Foreground", img2_fg)
cv2.imshow("Added", dst)

# Final Image
cv2.imshow('Result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

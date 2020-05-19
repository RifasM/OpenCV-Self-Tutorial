import cv2
import numpy as np

# ROI - Region of Interest
img = cv2.imread('../Media Files/input_images/img_2.jpg')

cv2.imshow("Original", img)
mod_img = img.copy()

ball = img[280:340, 330:390]                # Get pixels of ball from the region
mod_img[273:333, 100:160] = ball                # Write pixels of ball in new region

cv2.imshow("Modified", mod_img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()

# The B,G,R channels of an image can be split into their individual planes when needed.
# Then, the individual channels can be merged back together to form a BGR image again.
b, g, r = cv2.split(img)
# cv2.split() is a costly operation (in terms of time), so only use it if necessary.
# Numpy indexing is much more efficient and should be used if possible.

img_new_1 = cv2.merge((b, g, r))
# OR
img_new_2 = img[:, :, 0]                    # Greyscale
# array[row, column, column_selector]

# Suppose, you want to make all the red pixels to zero,
# you need not split like this and put it equal to zero.
# You can simply use Numpy indexing which is faster.
img_new_3 = img.copy()
img_new_3[:, :, 2] = 0                      # Make all red Pixels as 0
# OR
img_new_4 = img.copy()
img_new_4[..., 2] = 0                       # Another method of slicing

cv2.imshow("Original", img)
cv2.imshow("Using Split", img_new_1)
cv2.imshow("Using Index to convert to Greyscale", img_new_2)
cv2.imshow("Remove Red Pixels using slice", img_new_3)
cv2.imshow("Remove Red Pixels using different slice", img_new_4)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()

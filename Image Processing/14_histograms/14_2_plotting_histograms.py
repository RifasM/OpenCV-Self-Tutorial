import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
There are two ways for this,
Short Way : use Matplotlib plotting functions
Long Way : use OpenCV drawing functions
"""

# Using Matplotlib
img = cv2.imread('../../Media Files/input_images/img_5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.hist(x=grey_img.ravel(), bins=256, range=[0, 256])
plt.title("Matplotlib Histogram")
plt.show()

# OR
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title("BGP Histogram Plot")
plt.show()

# Using OpenCV (Not used Anymore)
"""
here you adjust the values of histograms along with its 
bin values to look like x,y coordinates so that you can 
draw it using cv2.line() or cv2.polyline() function to 
generate same image as above.
"""

# Mask
# create a mask
mask = np.zeros(grey_img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(src1=grey_img, src2=grey_img, mask=mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([grey_img], channels=[0], mask=None,
                         histSize=[256], ranges=[0, 256])
hist_mask = cv2.calcHist([grey_img], channels=[0], mask=mask,
                         histSize=[256], ranges=[0, 256])

plt.subplot(221), plt.title("Original"), plt.imshow(grey_img, 'gray')
plt.subplot(222), plt.title("Mask"), plt.imshow(mask, 'gray')
plt.subplot(223), plt.title("Masked Image"), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.title("Histogram"), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])

plt.show()

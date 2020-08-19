import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../../Media Files/input_images/img_6.jpg")

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

"""
You can see histogram lies in brighter region. 
We need the full spectrum. 
For that, we need a transformation function which 
maps the input pixels in brighter region to output 
pixels in full region. That is what histogram 
equalization does.
"""

# Now we find the minimum histogram value (excluding 0)
# and apply the histogram equalization equation
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

# Now we have the look-up table that gives us the
# information on what is the output pixel value
# for every input pixel value. So we just apply the transform.
img2 = cdf[img]

hist2, _ = np.histogram(img2.flatten(), 256, [0, 256])

cdf2 = hist2.cumsum()
cdf_normalized2 = cdf2 * hist2.max() / cdf2.max()

plt.plot(cdf_normalized2, color='b')
plt.hist(img2.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

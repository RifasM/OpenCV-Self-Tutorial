"""
In the first article, we calculated and plotted one-dimensional histogram.
It is called one-dimensional because we are taking only one feature into
our consideration, ie grayscale intensity value of the pixel.
But in two-dimensional histograms, you consider two features.
Normally it is used for finding color histograms where two
features are Hue & Saturation values of every pixel.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../../Media Files/input_images/img_1.jpg")
cv2.imshow("File", img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# 2D Histogram in OpenCV
"""
channels = [0,1] 
    because we need to process both H and S plane.
bins = [180,256] 
    180 for H plane and 256 for S plane.
range = [0,180,0,256] 
    Hue value lies between 0 and 180 & Saturation lies between 0 and 256.
"""
hist_cv = cv2.calcHist(images=[hsv],
                       channels=[0, 1],
                       mask=None,
                       histSize=[180, 256],
                       ranges=[0, 100, 0, 256])
print("Histogram Using CV2 Calc Hist:\n", hist_cv)

# 2D Histogram in Numpy
hist_np, xbins, ybins = np.histogram2d(hsv[..., 0].ravel(),
                                       hsv[..., 1].ravel(),
                                       [180, 256],
                                       [[0, 180],
                                        [0, 256]])
print("Histogram Using Numpy:\n", hist_np)

# Plotting 2D Histograms
"""
Method - 1 : Using cv2.imshow()
The result we get is a two dimensional array of size 180x256.
So we can show them as we do normally, using cv2.imshow() function.
It will be a grayscale image and it won’t give much idea what 
colors are there, unless you know the Hue values of different colors.

Method - 2 : Using Matplotlib
We can use matplotlib.pyplot.imshow() function to plot 2D histogram 
with different color maps. It gives us much more better idea about 
the different pixel density. But this also, doesn’t gives us idea
what color is there on a first look, unless you know the Hue 
values of different colors.
While using this function, remember, interpolation flag should be nearest for better results.
"""

plt.subplot(121), plt.title("OpenCV Plot"), plt.imshow(hist_cv, interpolation='nearest')
plt.subplot(122), plt.title("NumPy Plot"), plt.imshow(hist_np, interpolation='nearest')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

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

img = cv2.imread("../../Media Files/input_images/img_6.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2D Histogram in OpenCV
"""
channels = [0,1] 
    because we need to process both H and S plane.
bins = [180,256] 
    180 for H plane and 256 for S plane.
range = [0,180,0,256] 
    Hue value lies between 0 and 180 & Saturation lies between 0 and 256.
"""
hist = cv2.calcHist(images=[hsv],
                    channels=[0, 1],
                    mask=None,
                    histSize=[100, 256],
                    ranges=[0, 100, 0, 256])
print("Histogram Using CV2 Calc Hist:\n", hist)

# 2D Histogram in Numpy
hist, xbins, ybins = np.histogram2d(hsv[..., 0].ravel(),
                                    hsv[..., 1].ravel(),
                                    [180, 256],
                                    [[0, 180],
                                     [0, 256]])
print("Histogram Using Numpy:\n", hist)

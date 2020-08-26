"""
In the first article, we calculated and plotted one-dimensional histogram.
It is called one-dimensional because we are taking only one feature into
our consideration, ie grayscale intensity value of the pixel.
But in two-dimensional histograms, you consider two features.
Normally it is used for finding color histograms where two
features are Hue & Saturation values of every pixel.
"""

import cv2

img = cv2.imread("../../Media Files/input_images/img_6.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist(images=[hsv],
                    channels=[0, 1],
                    mask=None,
                    histSize=[100, 256],
                    ranges=[0, 100, 0, 256])
print("Histogram Using CV2 Calc Hist:\n", hist)

import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
 It is a plot with pixel values (ranging from 0 to 255, not always) 
 in X-axis and corresponding number of pixels in the image on Y-axis.
 Remember, this histogram is drawn for grayscale image, not color image).
 
 Histogram Terminology
 - DIMS - It is the number of parameters for which we collect the data. 
          In this case, we collect data regarding only one thing, 
          intensity value. So here it is 1.
 - BINS - It is the number of subdivisions in each dim.
 - RANGE - It is the range of intensity values you want to measure. 
           Normally, it is [0,256], ie all intensity values.
"""

"""
- Histogram Calculation in OpenCV
    SYNTAX: cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
    
    images : it is the source image of type uint8 or float32. 
            it should be given in square brackets, ie, “[img]”.
    channels : it is also given in square brackets. 
            It the index of channel for which we calculate histogram. 
            For example, if input is grayscale image, its value is [0]. 
            For color image, you can pass [0],[1] or [2] to calculate 
            histogram of blue,green or red channel respectively.
    mask : mask image. To find histogram of full image, it is given as “None”.
            But if you want to find histogram of particular region of image, 
            you have to create a mask image for that and give it as mask.
    histSize : this represents our BIN count. Need to be given in 
            square brackets. For full scale, we pass [256].
    ranges : this is our RANGE. Normally, it is [0,256].
"""
img = cv2.imread('../../Media Files/input_images/img_5.jpg')
blue_hist = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256],
                         ranges=[0, 256])
green_hist = cv2.calcHist(images=[img], channels=[1], mask=None, histSize=[256],
                          ranges=[0, 256])
red_hist = cv2.calcHist(images=[img], channels=[2], mask=None, histSize=[256],
                        ranges=[0, 256])
plt.subplot(2, 2, 1), plt.plot(blue_hist, color="b"), plt.title("Blue Histogram")
plt.subplot(2, 2, 2), plt.plot(green_hist, color="g"), plt.title("Green Histogram")
plt.subplot(2, 2, 3), plt.plot(red_hist, color="r"), plt.title("Red Histogram")
plt.subplot(2, 2, 4), plt.plot(blue_hist, color="b")
plt.subplot(2, 2, 4), plt.plot(green_hist, color="g")
plt.subplot(2, 2, 4), plt.plot(red_hist, color="r"), plt.title("Overlay")
plt.show()

grey_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
grey_hist = cv2.calcHist(images=[grey_image], channels=[0], mask=None, histSize=[256],
                         ranges=[0, 256])
plt.plot(grey_hist, color="black"), plt.title("Greyscale Image"), plt.show()

"""
Histogram Calculation in Numpy
    hist is same as we calculated before. But bins will have 257 elements, 
    because Numpy calculates bins as 0-0.99, 1-1.99, 2-2.99 etc. 
    So final range would be 255-255.99. To represent that, they also add 
    256 at end of bins. But we don’t need that 256. Upto 255 is sufficient.
"""
#  img.ravel()
#  returns contiguous flattened array(1D array with all the input-array
#  elements and with the same type as it). A copy is made only if needed.
hist, bins = np.histogram(a=img.ravel(), bins=256, range=[0, 256])
print(bins)
plt.plot(hist, color="black"), plt.title("Numpy Histogram"), plt.show()

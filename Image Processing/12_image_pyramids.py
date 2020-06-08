import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
There are two kinds of Image Pyramids. 
1) Gaussian Pyramid
    Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and columns 
    in Lower level (higher resolution) image. Then each pixel in higher level is formed by the contribution 
    from 5 pixels in underlying level with gaussian weights.
    By doing so, a M x N image becomes M/2 x N/2 image. So area reduces to one-fourth of original area. 
    It is called an Octave. The same pattern continues as we go upper in pyramid (ie, resolution decreases). 
    Similarly while expanding, area becomes 4 times in each level. 
    We can find Gaussian pyramids using cv2.pyrDown() and cv2.pyrUp() functions.
2) Laplacian Pyramids
    Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that. 
    Laplacian pyramid images are like edge images only. Most of its elements are zeros. 
    They are used in image compression. A level in Laplacian Pyramid is formed by the difference between that 
    level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid. 
"""
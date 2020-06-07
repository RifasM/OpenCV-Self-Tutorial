import cv2
import numpy as np

"""
OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr and Laplacian.

- Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. 
- You can also specify the size of kernel by the argument ksize. 
  If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter.
- Laplacian Derivative calculates the Laplacian of the image given by the relation, 
  \Delta src = \frac{\partial ^2{src}}{\partial x^2} + \frac{\partial ^2{src}}{\partial y^2}
"""
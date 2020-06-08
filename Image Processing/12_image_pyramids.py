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

# Image Blending using Pyramids

A = cv2.imread('../Media Files/input_images/img_14.jpg')
B = cv2.imread('../Media Files/input_images/img_15.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
print(A.shape)
real = np.hstack((A[:, :A.shape[0]//2], B[:, B.shape[0]//2:]))

cv2.imshow("Pyramid Blend", ls_)
cv2.imshow("Direct Blend", real)

cv2.waitKey(0)

cv2.imwrite('../Media Files/output_images/Pyramid_blending2.jpg', ls_)
cv2.imwrite('../Media Files/output_images/Direct_blending.jpg', real)

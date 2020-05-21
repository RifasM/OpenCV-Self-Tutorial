import cv2
import numpy as np

img1 = cv2.imread('../Media Files/input_images/img_2.jpg')

# cv2.getTickCount function returns the number of clock-cycles after a reference event
# So if you call it before and after the function execution,
# you get number of clock-cycles used to execute a function.

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()

# cv2.getTickFrequency function returns the frequency of clock-cycles,
# or the number of clock-cycles per second.
t = (e2 - e1)/cv2.getTickFrequency()
print("Execution Time", t, "ms")

# Check for optimisation by processor
print(cv2.useOptimized())

#  use cv2.useOptimized() to check if it is enabled/disabled and cv2.setUseOptimized() to enable/disable it

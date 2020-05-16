import numpy as np
import cv2

img = cv2.imread("input_images/img_1.jpg", 0)       # Load a color image in greyscale

cv2.imshow("Image", img)                            # Show the image on a frame
k = cv2.waitKey(0) & 0xFF                           # Wait for key press, since 64-bit machine, we AND the key with 0xFF
if k == 27:                                         # Check if ESC key is pressed
    cv2.destroyAllWindows()                         # Close all the open cv2 windows
elif k == ord('s'):                                 # Check if key pressed is s
    cv2.imwrite("output_images/img_1.png", img)     # Save the greyscale image as a png file
    cv2.destroyAllWindows()                         # Close all the open cv2 windows

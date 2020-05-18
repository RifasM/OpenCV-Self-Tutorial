# Create a Paint application with adjustable colors and brush radius using trackbars.

import numpy as np
import cv2

drawing = False
mode = True
ix, iy = -1, -1
color = [0, 0, 0]


def nothing(x):
    pass


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (color[0], color[1], color[2]), -1)
            else:
                cv2.circle(img, (x, y), 5, (color[0], color[1], color[2]), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (color[0], color[1], color[2]), -1)
        else:
            cv2.circle(img, (x, y), 5, (color[0], color[1], color[2]), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img=img, text="Press m to toggle Mode", org=(10, 500), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.namedWindow('Paint Application')
cv2.setMouseCallback('Paint Application', draw_circle)

cv2.createTrackbar('R', "Paint Application", 0, 255, nothing)
cv2.createTrackbar('G', 'Paint Application', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint Application', 0, 255, nothing)

while True:
    cv2.imshow('Paint Application', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four track bars
    color[2] = cv2.getTrackbarPos('R', 'Paint Application')
    color[1] = cv2.getTrackbarPos('G', 'Paint Application')
    color[0] = cv2.getTrackbarPos('B', 'Paint Application')

    cv2.imshow('Paint Application', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()

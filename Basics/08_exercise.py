# Create a Paint application with adjustable colors and brush radius using trackbars.

import numpy as np
import cv2

drawing = False
# 0 - Rectangle
# 1 - Line
# 2 - Circle
mode = [0, 1, 2]
ix, iy = -1, -1
color = [0, 0, 0]
m = 0
thickness = -1


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
            if mode[m] == 0:
                cv2.rectangle(img, (ix, iy), (x, y), (color[0], color[1], color[2]), thickness)
            elif mode[m] == 1:
                cv2.circle(img, (x, y), 5, (color[0], color[1], color[2]), thickness)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode[m] == 0:
            cv2.rectangle(img, (ix, iy), (x, y), (color[0], color[1], color[2]), thickness)
        elif mode[m] == 1:
            cv2.circle(img, (x, y), 5, (color[0], color[1], color[2]), thickness)
        else:
            cv2.circle(img, (x, y), 50, (color[0], color[1], color[2]), thickness)


img = np.zeros((1200, 700, 3), np.uint8)
cv2.putText(img=img, text="Press m to toggle Shapes", org=(10, 500), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
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

    shape = None
    if m == 0:
        shape = "Rectangle"
    elif m == 1:
        shape = "Line"
    else:
        shape = "Circle"

    cv2.imshow('Paint Application', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        m = (m + 1) % 3
    elif k == ord('t'):
        thickness = thickness + 1
    elif k == ord('l'):
        if thickness > 0:
            thickness = thickness - 1
    elif k == ord('f'):
        thickness = -1
    elif k == 27:
        break

    text = "Thickness: "+str(thickness)+" Object: "+shape
    cv2.rectangle(img, (10, 300), (600, 410), (0, 0, 0), -1)
    cv2.putText(img=img, text=text, org=(10, 400), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

cv2.destroyAllWindows()

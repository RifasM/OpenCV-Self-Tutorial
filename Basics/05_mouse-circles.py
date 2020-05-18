import cv2
import numpy as np

# Print all Available events in CV2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if flags:
        print("Mouse Clicked\nParameters: ", param)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Mouse Double Click')
cv2.setMouseCallback(window_name='Mouse Double Click', on_mouse=draw_circle, param=None)

while True:
    cv2.imshow('Mouse Double Click', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

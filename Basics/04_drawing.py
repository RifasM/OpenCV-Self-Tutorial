import numpy as np
import cv2


def show():
    cv2.imshow("Result", img)
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()
        exit(0)


img = np.zeros((512, 512, 3), np.uint8)                         # Create a black image

# Draw a diagonal blue line with thickness of 5 px
start = (0, 0)                                                  # Start at x=0, y=0
end = (511, 511)                                                # End at x=511, y=511
line_color = (255, 0, 0)                                        # Blue
line_thickness = 5                                              # default thickness = 1
img = cv2.line(img, start, end, line_color, line_thickness)
show()

# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle.
top = (384, 0)
bottom = (510, 128)
rectangle_color = (0, 255, 0)                                   # Green
rectangle_thickness = 3
img = cv2.rectangle(img, top, bottom, rectangle_color, rectangle_thickness)

show()

# To draw a circle, you need its center coordinates and radius.
center = (447, 63)
radius = 63
circle_color = (0, 0, 255)                                      # Red
circle_thickness = -1                                           # -1 to fill the circle with color
img = cv2.circle(img, center, radius, circle_color, circle_thickness)
show()

img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255),2,cv2.LINE_AA)

show()


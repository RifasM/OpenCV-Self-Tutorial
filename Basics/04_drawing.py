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
img = cv2.line(img=img, pt1=start, pt2=end, color=line_color, thickness=line_thickness)
show()

# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle.
top = (384, 0)
bottom = (510, 128)
rectangle_color = (0, 255, 0)                                   # Green
rectangle_thickness = 3
img = cv2.rectangle(img=img, pt1=top, pt2=bottom, color=rectangle_color, thickness=rectangle_thickness)

show()

# To draw a circle, you need its center coordinates and radius.
circle_center = (447, 63)
radius = 63
circle_color = (0, 0, 255)                                      # Red
circle_thickness = -1                                           # -1 to fill the circle with color
img = cv2.circle(img=img, center=circle_center, radius=radius, color=circle_color, thickness=circle_thickness)
show()


# Draw an ellipse with center, axis, angle of rotation (anti-clockwise), angle of arc(clockwise)
ellipse_center = (256, 256)
axis = (100, 50)                                                 # x axis length = 100, y axis length = 50
angle_rotation = 0                                               # No rotation
angle_start = 0                                                  # Start at 0
angle_end = 180                                                  # Draw half an ellipse
ellipse_color = (255, 0, 0)                                      # Blue
ellipse_thickness = -1
img = cv2.ellipse(img=img, center=ellipse_center, axes=axis,
                  angle=angle_rotation, startAngle=angle_start,
                  endAngle=angle_end, color=ellipse_color, thickness=ellipse_thickness)
show()

# To draw a polygon, first you need coordinates of vertices.
# Make those points into an array of shape ROWSx1x2 where
# ROWS are number of vertices and it should be of type int32
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
points = [pts]                                                  # Create an array of points to plot
polygon_color = (0, 255, 255)                                   # Yellow
img = cv2.polylines(img=img, pts=[pts], isClosed=True, color=polygon_color)
show()

# Adding Text to the image
font = cv2.FONT_HERSHEY_SIMPLEX                                 # Font family to use
text = "Self Tutorial"                                          # Text to display
origin = (10, 500)                                              # Origin of text, bottom-left corner
font_scale = 2                                                  # Font Scaling Factor
text_color = (255, 255, 255)                                    # White
# https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#line
type_line = cv2.LINE_AA                                         # Type of line, Anti Aliased line(AA)
cv2.putText(img=img, text=text, org=origin, fontFace=font, fontScale=font_scale,
            color=text_color, thickness=2, lineType=type_line)
show()


import cv2

cap = cv2.VideoCapture('../Media Files/input_videos/vid_1.mp4')            # Open a video file, 0 to open Web-Cam

while cap.isOpened():                                       # Check if cap is initialized and then proceed looping
    ret, frame = cap.read()                                 # returns True, frame if frame is available, else False

    if not ret:                                             # If ret is false, break out of loop
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          # Convert to greyscale image

    cv2.imshow('Grey-scaled', gray)                         # Show the GreyScale Image
    if cv2.waitKey(1) & 0xFF == ord('q'):                   # Wait for key press and check if key pressed is q
        break                                               # if True, break out of the video loop

cap.release()                                               # Release all resources allocated to cap
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture('../Media Files/input_videos/vid_1.mp4')  # Open a video file

# Changing the video properties (0 to 18), given in:
# http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
# cap.set(3, 320)     # Setting width to 320
# cap.set(4, 240)     # Setting height to 240

# More about Fourcc https://en.wikipedia.org/wiki/FourCC
fourcc = cv2.VideoWriter_fourcc(*'XVID')                    # Set Video format to XVID
frame_size = (1280, 720)                                     # Set Output video frame size to 640 x 480
file_name = "../Media Files/output_videos/vid_1.avi"                       # Output file name
frames_per_second = 20                                      # Number of frames to save per second

out = cv2.VideoWriter(file_name, fourcc, frames_per_second, frame_size)         # Video Writer Object

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Original', frame)

        # 0 -> Horizontally Flip
        # 1 -> Vertically Flip
        # -1 -> Flip on both axis
        frame = cv2.flip(frame, 1)                          # Flip the frame
        out.write(frame)                                    # Write the flipped frame

        cv2.imshow('Flipped', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()                                               # Release output video memory
cv2.destroyAllWindows()

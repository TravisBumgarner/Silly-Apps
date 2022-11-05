import pyvirtualcam
import cv2
from imutils.video import VideoStream
import imutils

# These values should match your webcam. 
WIDTH = 1920
HEIGHT = 1080

# # Unclear how to capture the correct webcam here. 
for i_src in range(0,4):
    vs = VideoStream(src=i_src).start() # Will need to find the src that matches your webcam. Unclear how to iterate on this. 
    img = vs.read()
    height = len(img)
    width = len(img[0])
    if not height == HEIGHT and not width == WIDTH:
        vs.stop()
    else:
        print(f'using index {i_src}')
        break


with pyvirtualcam.Camera(width=WIDTH, height=HEIGHT, fps=60) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        img = vs.read()
        img = imutils.resize(img, width=WIDTH, height=HEIGHT)
        img = imutils.opencv2matplotlib(img) 
        cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # My Webcam sends RGB but we need BGR. 
        cam.send(img)
        cam.sleep_until_next_frame()
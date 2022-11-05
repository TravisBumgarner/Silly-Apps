import pyvirtualcam
import cv2
from imutils.video import VideoStream
import imutils
from themes import *

# These values should match your webcam. 
CAM_WIDTH = 1920
CAM_HEIGHT = 1080

OUTPUT_WIDTH = 480
OUTPUT_HEIGHT = 270

for i_src in range(0,4):
    vs = VideoStream(src=i_src).start() # Will need to find the src that matches your webcam. Unclear how to iterate on this. 
    img = vs.read()
    height = len(img)
    width = len(img[0])
    if not height == CAM_HEIGHT and not width == CAM_WIDTH:
        vs.stop()
    else:
        print(f'using index {i_src}')
        break


with pyvirtualcam.Camera(width=OUTPUT_WIDTH, height=OUTPUT_HEIGHT, fps=30) as cam:
    while True:
        img = vs.read()
        img = imutils.resize(img, width=OUTPUT_WIDTH, height=OUTPUT_HEIGHT)
        img = imutils.opencv2matplotlib(img) 

        # img = gameboy(img)
        img = theme_black_and_white(img)
        
        # Webcam sends RGB but we need BGR. 
        cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cam.send(img)
        cam.sleep_until_next_frame()

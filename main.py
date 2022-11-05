import pyvirtualcam
import cv2
from imutils.video import VideoStream
import imutils
import numpy as np

# These values should match your webcam. 
WIDTH = 1920
HEIGHT = 1080

def gameboy(img):
    colors = [
        [155, 188, 15],
        [48, 246, 35],
        [139, 172, 15],
        [15, 56, 15]
    ]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    grayscale_buckets = img
    # Convert 0 -> 255 to 0 -> 3
    bucket_segments = 255 / len(colors)
    grayscale_buckets = np.rint(np.divide(grayscale_buckets, bucket_segments))
    grayscale_buckets.astype(np.uint8)

    color_buckets = grayscale_buckets[:, :, np.newaxis] * np.ones((HEIGHT, WIDTH, 3)).astype(np.uint8)

    for i in range(len(colors)):
        color_buckets = np.where(color_buckets == [i, i, i], np.array(colors[i]), color_buckets)

    color_buckets = color_buckets.astype(np.uint8)

    return color_buckets

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


with pyvirtualcam.Camera(width=WIDTH, height=HEIGHT, fps=30) as cam:
    print(f'Using virtual camera: {cam.device}')
    while True:
        img = vs.read()
        img = imutils.resize(img, width=WIDTH, height=HEIGHT)
        img = imutils.opencv2matplotlib(img) 

        img = gameboy(img)
        
        cv2.cvtColor(img, cv2.COLOR_RGB2BGR) # My Webcam sends RGB but we need BGR. 
        cam.send(img)
        cam.sleep_until_next_frame()
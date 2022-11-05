import cv2
import numpy as np


def gameboy(img):
    colors = [
        [15, 56, 15], # Darkest
        [48, 98, 48], # Darker
        [139, 172, 15], # Light 
        [155, 188, 15], # Lightest
    ]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    grayscale_buckets = img
    # Convert 0 -> 255 to 0 -> 3
    bucket_segments = 255 / len(colors)
    grayscale_buckets = np.rint(np.divide(grayscale_buckets, bucket_segments))
    grayscale_buckets.astype(np.uint8)

    height = len(grayscale_buckets)
    width = len(grayscale_buckets[0])

    color_buckets = grayscale_buckets[:, :, np.newaxis] * np.ones((height, width, 3)).astype(np.uint8)

    for i in range(len(colors)):
        color_buckets = np.where(color_buckets == [i, i, i], np.array(colors[i]), color_buckets)

    color_buckets = color_buckets.astype(np.uint8)

    return color_buckets
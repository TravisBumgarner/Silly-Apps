import cv2
import numpy as np

def theme_method_colors_by_brightness(img, colors, colors_repeated=1):
    """
    Map the array passed in of colors = [darkest, darker, medium, lighter, lightest] to the bucketed greyscale values from 0 -> 255
    
    Keyword Arguments
    
    colors_repeated = will repeat the array of colors passed in n times (default = 1)
    """
    colors = colors * colors_repeated
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    grayscale_buckets = img
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


def theme_gameboy(img):
    colors = [
        [15, 56, 15], # Darkest
        [48, 98, 48], # Darker
        [139, 172, 15], # Light 
        [155, 188, 15], # Lightest
    ]
    return theme_method_colors_by_brightness(img, colors)

def theme_beach(img):
    colors = [
        [238, 184, 104],
        [73, 190, 170],
        [239, 118, 122],
        [69, 105, 144],
    ]
    return theme_method_colors_by_brightness(img, colors)

def theme_deep_beach(img):
    colors = [
        [238, 184, 104],
        [73, 190, 170],
        [239, 118, 122],
        [69, 105, 144],
    ]
    return theme_method_colors_by_brightness(img, colors, colors_repeated=2)

def theme_black_and_white(img):
    colors = [
        [0,0,0],
        [127,127,127],
        [255,255,255],
    ]
    return theme_method_colors_by_brightness(img, colors)
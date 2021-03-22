#!/usr/bin/env python

"""02.GreenScreen.py
Join a background to an image with a large green area."""

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2021, OpenCV-projects-with-Python"
__licence__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all@gmail.com"
__status__ = "Production"

import numpy as np
import cv2

# Original image and Background image
path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/green_screen.jpg"
imageOriginal = cv2.imread(path)
print("Original Dimensions: ", imageOriginal.shape)

path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/praiaNazare.jpg"
imageBackground = cv2.imread(path)
print("Background Dimensions: ", imageBackground.shape)

# Preserve Aspect Ratio - Downscale process
scale_percent = 40  # percent of original size
height = int(imageOriginal.shape[0] * scale_percent / 100)
width = int(imageOriginal.shape[1] * scale_percent / 100)
dim = (width, height)

# Resized images - Original and Background
imageResized = cv2.resize(imageOriginal, dim, interpolation=cv2.INTER_AREA)
print("Resized Dimensions: ", imageResized.shape)

resize_x, resize_y = imageResized.shape[0], imageResized.shape[1]
dimBackground = (resize_y, resize_x)
imageBackgroundResized = cv2.resize(imageBackground, dimBackground)
print("Resized Background Dimensions: ", imageBackgroundResized.shape)

# Threshold - Green
lowerGreen = np.array([0, 170, 0])
upperGreen = np.array([120, 180, 120])
mask = cv2.inRange(imageResized, lowerGreen, upperGreen)

# Green masked area
copyMask = np.copy(imageResized)
copyMask[mask != 0] = [0, 0, 0]

# Background masked area
copyBackground = np.copy(imageBackgroundResized)
copyBackground[mask == 0] = [0, 0, 0]

# Image Final
imageFinal = copyMask + copyBackground


# Same size  and horizontally
def concat_vh(list_2d):
    # return final image
    return cv2.vconcat([cv2.hconcat(list_h)
                        for list_h in list_2d])


# Function calling (concat_vh)
img_tile = concat_vh([[imageResized, imageBackgroundResized],
                      [copyMask, imageFinal]])

cv2.imshow('Green Screen', img_tile)


cv2.waitKey(0)
cv2.destroyAllWindows()

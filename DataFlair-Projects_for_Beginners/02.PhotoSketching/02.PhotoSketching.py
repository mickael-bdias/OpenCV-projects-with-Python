#!/usr/bin/env python

"""02.PhotoSketching.py:
 Computer vision can be used to process images and perform various transformations on the image.
 The idea is to build an app that will take an image as OutputPictures from the user and convert it into a pencil sketching.
 Input from the user."""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"

# Hide GUI (TKinter)
Tk().withdraw()

# Ask user for Original image
path = askopenfilename(title="Select a file", filetypes=[("jpg files", "*.jpg"), ("png files", "*.png"),
                                                         ("all files", "*.*")])
print(path)
imageOriginal = cv2.imread(path)
print("Original Dimensions: ", imageOriginal.shape)

# Preserve Aspect Ratio - Downscale process
scale_percent = 20  # percent of original size
height = int(imageOriginal.shape[0] * scale_percent / 100)
width = int(imageOriginal.shape[1] * scale_percent / 100)
dim = (width, height)

# Resized image
imageResized = cv2.resize(imageOriginal, dim, interpolation=cv2.INTER_AREA)
print("Resized Dimensions: ", imageResized.shape)

# Edge functions
imageLaplacian = cv2.Laplacian(src=imageResized, ddepth=cv2.CV_8U, ksize=3)
imageDetailEnhance = cv2.detailEnhance(imageLaplacian, sigma_s=60, sigma_r=0.07)
imageGray = cv2.cvtColor(imageDetailEnhance, cv2.COLOR_BGR2GRAY)
imageInvertColors = 255 - imageGray  # Grayscale images are 8 bit images or have a maximum of 256 tones.

cv2.imshow('Photo Sketching', imageInvertColors)

cv2.waitKey(0)
cv2.destroyAllWindows()

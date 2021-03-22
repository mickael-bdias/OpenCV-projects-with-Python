#!/usr/bin/env python

"""01.PixelGrid.py
Images are numerical data. It is possible to change the value of a pixel.
This script contains two plots - Gray and Changed value."""

import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2021, OpenCV-projects-with-Python"
__licence__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all@gmail.com"
__status__ = "Production"

# Original image
path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/IMG_20200911_172937.jpg"
imageOriginal = mpimg.imread(path)
print("Original Dimensions: ", imageOriginal.shape)

# Preserve Aspect Ratio - Downscale process
scale_percent = 10  # percent of original size
height = int(imageOriginal.shape[0] * scale_percent / 100)
width = int(imageOriginal.shape[1] * scale_percent / 100)
dim = (width, height)

# Resized image
imageResized = cv2.resize(imageOriginal, dim, interpolation=cv2.INTER_AREA)
print("Resized Dimensions: ", imageResized.shape)

# Convert resized image to gray and plot
imageGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
print("imageColorSwitch Dimensions: ", imageGray.shape)
plt.title("Image Gray")
plt.imshow(imageGray, cmap='gray')
plt.show()

# Add value to image (numpy) and plot
addValue = 2
copiedImage = imageGray.copy()
changedValuePixel = copiedImage + addValue
plt.imshow(changedValuePixel, cmap='gray')
plt.title("Pixel value changed")
plt.show()

# Values of the pixel
x, y = 200, 200
print("Before add value (imageGray): ", imageGray[y, x])
print("After add value (changedValuePixel): ", changedValuePixel[y, x])

cv2.waitKey(0)
cv2.destroyAllWindows()

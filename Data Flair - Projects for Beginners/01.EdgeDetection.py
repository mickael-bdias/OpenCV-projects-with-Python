#!/usr/bin/env python

"""01.EdgeDetection.py:
 The Python opencv library is mostly preferred for computer vision tasks.
 You can detect all the edges of different objects of the image."""

import cv2
import numpy as np
import Auxiliary_scripts.StackImages


__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Development"

path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/IMG_20200911_172937.jpg"
imageOriginal = cv2.imread(path)
print("Original Dimensions: ", imageOriginal.shape)

# Preserve Aspect Ratio - Downscale
scale_percent = 10  # percent of original size
height = int(imageOriginal.shape[0] * scale_percent / 100)
width = int(imageOriginal.shape[1] * scale_percent / 100)
dim = (width, height)

# Resized image
imageResized = cv2.resize(imageOriginal, dim, interpolation=cv2.INTER_AREA)
print("Resized Dimensions: ", imageResized.shape)
cv2.imshow("Resized", imageResized)
print(imageResized.shape)

# Gray image
imageGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", imageGray)
print(imageGray.shape)

# Blur image
imageBlur = cv2.GaussianBlur(imageGray, (3, 3), cv2.BORDER_DEFAULT)
cv2.imshow("Blur", imageBlur)

imageCanny = cv2.Canny(imageBlur, 150, 200, cv2.BORDER_DEFAULT)
cv2.imshow("Canny", imageCanny)

imageSobel_X = cv2.Sobel(imageBlur, cv2.CV_32F, 1, 0, ksize=3)
cv2.imshow("Sobel X", imageSobel_X)

imageSobel_Y = cv2.Sobel(imageBlur, cv2.CV_32F, 0, 1, ksize=3)
cv2.imshow("Sobel Y", imageSobel_Y)

imageLaplacian = cv2.Laplacian(src=imageBlur, ddepth=cv2.CV_8U, ksize=3)
cv2.imshow("Laplacian", imageLaplacian)

StackedImages = Auxiliary_scripts.StackImages(0.5, ([imageBlur, imageCanny]))
cv2.imshow("Stacked Images", StackedImages)

cv2.waitKey(0)
cv2.destroyAllWindows()

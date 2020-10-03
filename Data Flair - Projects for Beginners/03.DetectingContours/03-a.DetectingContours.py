#!/usr/bin/env python

"""03-a.DetectingContours.py:
 Contours are outlines or the boundaries of the shape.
 You can build a project to detect certain types of shapes.
 For example: with a round shape, you can detect all the coins present in the image.
 The project is good to understand how to detect objects with different kinds of shapes.
 approxPolyDP() and findContours() methods.
 Note: for contour loop from authentise."""

import cv2

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"

# Original image
path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/euro_money.jpg"
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
imageGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (5, 5), cv2.BORDER_DEFAULT)
# imageBlurBilateral = cv2.bilateralFilter(imageGray, 5, 175, 175, cv2.BORDER_DEFAULT)  # Better to preserve edges
imageCanny = cv2.Canny(imageBlur, 80, 150, cv2.BORDER_DEFAULT)

# Finding Contours
contours, hierarchy = cv2.findContours(imageCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# approxPolyDP
contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    area = cv2.contourArea(contour)
    if (len(approx) > 8) & (len(approx) < 23) & (area > 30):  # polygons with greater than 8 vertices
        contour_list.append(contour)

# Draw Contours
cv2.drawContours(imageResized, contour_list, -1, (230, 153, 0), 2)  # rgb(0, 153, 230)
cv2.imshow('Detecting Contours', imageResized)

cv2.waitKey(0)
cv2.destroyAllWindows()

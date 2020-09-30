#!/usr/bin/env python

"""03-b.DetectingContours.py:
 Contours are outlines or the boundaries of the shape.
 You can build a project to detect certain types of shapes.
 For example: with a round shape, you can detect all the coins present in the image.
 The project is good to understand how to detect objects with different kinds of shapes.
 HoughCircles() method and matplotlib.
 Note: for co loop from thepythoncode"""

import cv2
import matplotlib.pyplot as plt

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"

# Original image
path = "/Resources/Images/euro_money.jpg"
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
imageColorSwitch = cv2.cvtColor(imageResized, cv2.COLOR_BGR2RGB)
imageGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (5, 5), cv2.BORDER_DEFAULT)
# imageBlurBilateral = cv2.bilateralFilter(imageGray, 5, 175, 175, cv2.BORDER_DEFAULT)  # Better to preserve edges

# HoughCircles
circles = cv2.HoughCircles(image=imageBlur, method=cv2.HOUGH_GRADIENT, dp=0.9,
                           minDist=80, param1=110, param2=39, maxRadius=70)

# Copy of imageColorSwitch, to draw the detected circles
cimg = imageColorSwitch.copy()

# Draw circles
for co, i in enumerate(circles[0, :], start=1):
    cv2.circle(cimg, (i[0], i[1]), 2, (255, 0, 0), 2)  # draw the outer circle in green
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)  # draw the center of the circle in red

# Show circles
print("Number of circles detected:", co)
cv2.imwrite("coins_circles_detected.png", cimg)  # Save the image, convert to BGR to save with proper colors
plt.imshow(cimg)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

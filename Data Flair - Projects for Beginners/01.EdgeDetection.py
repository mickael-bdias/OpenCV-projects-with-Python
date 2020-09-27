#!/usr/bin/env python

"""01.EdgeDetection.py:
 The Python opencv library is mostly preferred for computer vision tasks.
 You can detect all the edges of different objects of the image.
 Note: concat_vh function from Geeks for Geeks"""

import cv2

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"

# Original image
path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/IMG_20200911_172937.jpg"
imageOriginal = cv2.imread(path)
print("Original Dimensions: ", imageOriginal.shape)

# Preserve Aspect Ratio - Downscale process
scale_percent = 10  # percent of original size
height = int(imageOriginal.shape[0] * scale_percent / 100)
width = int(imageOriginal.shape[1] * scale_percent / 100)
dim = (width, height)

# Resized image
imageResized = cv2.resize(imageOriginal, dim, interpolation=cv2.INTER_AREA)
print("Resized Dimensions: ", imageResized.shape)
# cv2.imshow("Resized", imageResized)
print(imageResized.shape)

# Edge functions
imageGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (3, 3), cv2.BORDER_DEFAULT)
imageCanny = cv2.Canny(imageBlur, 150, 200, cv2.BORDER_DEFAULT)
imageSobel_X = cv2.Sobel(imageBlur, cv2.CV_8U, 1, 0, ksize=3)  # works with CV_8U not CV_32F
imageSobel_Y = cv2.Sobel(imageBlur, cv2.CV_8U, 0, 1, ksize=3)
imageLaplacian = cv2.Laplacian(src=imageBlur, ddepth=cv2.CV_8U, ksize=3)


# Same size  and horizontally
def concat_vh(list_2d):
    # return final image
    return cv2.vconcat([cv2.hconcat(list_h)
                        for list_h in list_2d])


# Function calling (concat_vh)
img_tile = concat_vh([[imageGray, imageBlur, imageCanny],
                      [imageSobel_X, imageSobel_Y, imageLaplacian]])

cv2.imshow('Edge Detection', img_tile)

cv2.waitKey(0)
cv2.destroyAllWindows()

#!/usr/bin/env python

"""04.ResizeImages.py:
 The first step to build a collage of your pictures and generate with them an only picture similar to a mosaic.
 You need to create two directories, one for the original pictures, and the other for the resized pictures.
 In the case, it's the directories OriginalPictures and ResizedPictures.
 You need also to define the directories path.
 Change the original and resized relation size in fx and fy.
 Note: If the images have big dimensions, it is no need to the fx and fy have more than 0.5."""

import glob
import cv2
import os

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"

# Directory of the original pictures
originalPath = glob.glob("C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Data Flair - Projects for "
                         "Beginners/04.CollageMosaicGenerator/OriginalPictures//*.jpg")

# Directory of the saved (resized) pictures
resizedPath = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Data Flair - Projects for " \
              "Beginners/04.CollageMosaicGenerator/ResizedPictures "

# Change directory to save the resized pictures to resizedPath
os.chdir(resizedPath)

counter = 0
cv_img = []

for img in originalPath:
    counter += 1
    originalImage = cv2.imread(img)
    cv_img.append(originalImage)
    print("Original Dimensions: " + str(img), originalImage.shape)
    resizedImage = cv2.resize(originalImage, None, fx=0.7, fy=0.7)
    print("Resized Dimensions: " + str(img), resizedImage.shape)
    cv2.imwrite("ResizedImage_" + str(counter).zfill(4) + '.jpg', resizedImage)

cv2.destroyAllWindows()

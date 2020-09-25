#!/usr/bin/env python

"""01.EdgeDetection.py:
 The Python opencv library is mostly preferred for computer vision tasks.
 You can detect all the edges of different objects of the image."""

import cv2


__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Development"

path = "Resources/Images/lena.png"
print(path)
image = cv2.imread(path)
print(image)


cv2.waitKey(0)

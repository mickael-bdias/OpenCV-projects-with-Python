#!/usr/bin/env python

"""03.GreenScreen.py
Comparison between RGB and HSV.
Used matplotlib to plot the 6 channels"""

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2021, OpenCV-projects-with-Python"
__licence__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all@gmail.com"
__status__ = "Production"

import matplotlib.pyplot as plt
import cv2

# Original image and Background image
path = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Resources/Images/colors_houses.jpg"
imageOriginal = cv2.imread(path)
print("Original Dimensions: ", imageOriginal.shape)

# RGB channels
redChannel = imageOriginal[:, :, 0]
greenChannel = imageOriginal[:, :, 1]
blueChannel = imageOriginal[:, :, 2]

# HSV channels
hsv = cv2.cvtColor(imageOriginal, cv2.COLOR_RGB2HSV)
hueChannel = hsv[:, :, 0]
saturationChannel = hsv[:, :, 1]
valueChannel = hsv[:, :, 2]

# Plot RGB and HSV channels
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(20, 10))

ax1.set_title('Red')
ax1.imshow(redChannel, cmap='gray')
ax2.set_title('Green')
ax2.imshow(greenChannel, cmap='gray')
ax3.set_title('Blue')
ax3.imshow(blueChannel, cmap='gray')

ax4.set_title('Hue')
ax4.imshow(hueChannel, cmap='gray')
ax5.set_title('Saturation')
ax5.imshow(saturationChannel, cmap='gray')
ax6.set_title('Value')
ax6.imshow(valueChannel, cmap='gray')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

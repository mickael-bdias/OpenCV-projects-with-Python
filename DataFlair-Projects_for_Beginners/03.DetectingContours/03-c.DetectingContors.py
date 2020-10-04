#!/usr/bin/env python

"""03-c.DetectingContours.py:
 Contours are outlines or the boundaries of the shape.
 You can build a project to detect certain types of shapes.
 For example: with a round shape, you can detect all the coins present in the image.
 The project is good to understand how to detect objects with different kinds of shapes.
 approxPolyDP() and findContours() methods.
 Camara OutputPictures
 Note: for contour loop from authentise."""

import cv2

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"

# Frame dimensions and set camara
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, imageCamara = cap.read()

    # ESC button to break the while loop
    escapeButton = 27

    # Edge functions
    imageGray = cv2.cvtColor(imageCamara, cv2.COLOR_BGR2GRAY)
    imageBlurBilateral = cv2.bilateralFilter(imageGray, 5, 175, 175, cv2.BORDER_DEFAULT)  # Better to preserve edges
    imageCanny = cv2.Canny(imageBlurBilateral, 180, 200, cv2.BORDER_DEFAULT)

    # Finding Contours
    contours, hierarchy = cv2.findContours(imageCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # approxPolyDP
    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        area = cv2.contourArea(contour)
        if (len(approx) > 8) & (len(approx) < 16) & (area > 30):  # polygons with greater than 8 vertices
            contour_list.append(contour)

    # Draw Contours
    cv2.drawContours(imageCamara, contour_list, -1, (230, 153, 0), 2)  # rgb(0, 153, 230)
    cv2.drawContours(imageBlurBilateral, contour_list, -1, (0, 0, 0), 2)

    cv2.imshow("Camara", imageCamara)
    cv2.imshow("Edges", imageBlurBilateral)

    if cv2.waitKey(1) & 0xFF == escapeButton:  # For 'q' use: ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

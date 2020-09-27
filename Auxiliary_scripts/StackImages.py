#!/usr/bin/env python

"""StackImages.py:
 Function to stack images and video.
 Made by Murtaza Hassen. GitHub: murtazahassan/OpenCV-Python-Tutorials-and-Projects/blob/master/Basics/
 Joining_Multiple_Images_To_Display.py.
 Note: stack_images function has been modified."""

import cv2
import numpy as np

__author__ = "Murtaza Hassen"
__copyright__ = "Copyright 2020, OpenCV-Python-Tutorials-and-Projects"
__maintainer__ = "Murtaza Hassen"
__email__ = "contact@murtazahassan.com"
__status__ = "Production"

frameWidth = 320 # 640
frameHeight = 240  # 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


def stack_images(img_array, scale, labels=[]):
    size_w = img_array[0][0].shape[1]
    size_h = img_array[0][0].shape[0]
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                img_array[x][y] = cv2.resize(img_array[x][y], (size_w, size_h), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        hor_con = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
            hor_con[x] = np.concatenate(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            img_array[x] = cv2.resize(img_array[x], (size_w, size_h), None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    if len(labels) != 0:
        each_img_width = int(ver.shape[1] / cols)
        each_img_height = int(ver.shape[0] / rows)
        print(each_img_height)
        for d in range(0, rows):
            for c in range(0, cols):
                cv2.rectangle(ver, (c * each_img_width, each_img_height * d),
                              (c * each_img_width + len(labels[d][c]) * 13 + 27, 30 + each_img_height * d),
                              (255, 255, 255), cv2.FILLED)
                cv2.putText(ver, labels[d][c], (each_img_width * c + 10, each_img_height * d + 20),
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 255), 2)
    return ver


while True:
    success, imageCamara = cap.read()

    # ESC button to break the while loop
    escapeButton = 27

    # Edge functions
    imageGray = cv2.cvtColor(imageCamara, cv2.COLOR_BGR2GRAY)
    imageBlur = cv2.GaussianBlur(imageGray, (3, 3), cv2.BORDER_DEFAULT)
    imageCanny = cv2.Canny(imageBlur, 150, 200, cv2.BORDER_DEFAULT)
    imageLaplacian = cv2.Laplacian(src=imageBlur, ddepth=cv2.CV_8U, ksize=3)
    imageLaplacian_2 = cv2.Laplacian(src=imageBlur, ddepth=cv2.CV_8U, ksize=5)
    imageSobel_X = cv2.Sobel(imageBlur, cv2.CV_8U, 1, 0, ksize=3)
    imageSobel_Y = cv2.Sobel(imageBlur, cv2.CV_8U, 0, 1, ksize=3)

    imageBlank = np.zeros((200, 200), np.uint8)
    StackedImages = stack_images(([imageCamara, imageGray, imageBlur],
                                  [imageCanny, imageLaplacian, imageLaplacian_2]), 0.5)
    cv2.imshow("Staked Images", StackedImages)

    if cv2.waitKey(1) & 0xFF == escapeButton:  # For 'q' use: ord('q'):
        break

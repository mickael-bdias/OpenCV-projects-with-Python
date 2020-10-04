#!/usr/bin/env python

"""04.CollagePhotoMosaic.py:
 The second step to build a collage of your pictures and generate with them an only picture similar to a mosaic.
 You need to name your target image (in the ResizedPictures directory).
 In that case, it's the target.jpg.
 You need to create one directory for the output pictures.
 In the case, it's the directory OutputPictures.
 There are 4 input parameters: use_shuffle, inputs_limit, img_size, pixel_per_img.
 The img_size parameter do not need to have more than 60.
 Increasing this number will increasing the MB of the output image.
 Note: Code inspired by jayin92 in it's PhotoMosaic project.
       It was modified but most of main ideas remain"""

import cv2
import numpy as np
import os
import random

__author__ = "Mickaël Dias"
__copyright__ = "Copyright 2020, OpenCV-projects-with-Python"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Mickaël Dias"
__email__ = "industry4.0all.gmail.com"
__status__ = "Production"


def adjust_color(img, b, g, r):
    # Change color of the pictures to match the target picture. print(b, g, r)
    tmp_img = img / 256  # 8-bit color
    tmp_img[:, :, 0] = tmp_img[:, :, 0] ** (1 - b / 255)
    tmp_img[:, :, 1] = tmp_img[:, :, 1] ** (1 - g / 255)
    tmp_img[:, :, 2] = tmp_img[:, :, 2] ** (1 - r / 255)

    tmp_img = tmp_img * 256

    return tmp_img.astype('int32')


def crop_and_resize(img, resize_size):
    # Crop and Resize
    w = img.shape[0]
    h = img.shape[1]
    crop_size = min(w, h)
    img = img[int(w / 2 - crop_size / 2):
              int(w / 2 + crop_size / 2), int(h / 2 - crop_size / 2):int(h / 2 + crop_size / 2)]

    img = cv2.resize(img, (resize_size, resize_size))

    return img


def combine(target, inputs, inputs_size, per_pixel):
    w = target.shape[0]
    h = target.shape[1]

    print(inputs[0].shape)

    output = np.zeros((w * inputs_size // per_pixel, h * inputs_size // per_pixel, 3))
    inputs_len = len(inputs)
    r = 0
    t = 0
    idx = 0
    for i in range(h // per_pixel):
        for j in range(w // per_pixel):
            output[r:r + inputs_size, t:t + inputs_size] = adjust_color(inputs[idx % inputs_len],
                                                                        target[j * per_pixel, i * per_pixel, 0],
                                                                        target[j * per_pixel, i * per_pixel, 1],
                                                                        target[j * per_pixel, i * per_pixel, 2])
            r += inputs_size
            idx += 1
        t += inputs_size
        r = 0

    return output


if __name__ == "__main__":

    # Parameters
    use_shuffle = True
    inputs_limit = -1  # -1 for not limited
    img_size = 40
    pixel_per_img = 3

    # Paths
    pathTargetImage = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Data Flair - Projects for " \
                      "Beginners/04.CollageMosaicGenerator/ResizedPictures/target.jpg"
    pathDirectory = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Data Flair - Projects for " \
                    "Beginners/04.CollageMosaicGenerator/ResizedPictures"
    pathOutput = "C:/Users/Mickael/PycharmProjects/OpenCV-projects-with-Python/Data Flair - Projects for " \
                 "Beginners/04.CollageMosaicGenerator/OutputPictures"

    inputs = []

    # Verify file and main process
    if os.path.isfile(pathTargetImage):
        print("File 'target.jpg' exist")
        for item in os.listdir(pathDirectory):
            if inputs_limit != -1 and len(inputs) >= inputs_limit:
                break
            try:
                print("load {} successfully.".format(item))
                inputs.append(crop_and_resize(cv2.imread(os.path.join(pathDirectory, item)), img_size))
            except:
                print("{} is not an image.".format(item))
        if use_shuffle:
            random.shuffle(inputs)
    else:
        print("File 'target.jpg' don´t exist")

    # Output the target image
    print("complete load inputs image.")
    imageTarget = cv2.imread(pathTargetImage)
    output = combine(imageTarget, inputs, img_size, pixel_per_img)

    # Change directory to save the target image to pathOutput
    os.chdir(pathOutput)

    # Save the target image and resize to create an A4 poster
    for img in pathOutput:
        cv2.imwrite("PhotoMosaicColor.jpg", output)
        print("Original Dimensions: " + str(img), output.shape)
        # resizedImage = cv2.resize(output, (3508, 2480))  # A4 size horizontal
        resizedImage = cv2.resize(output, (2480, 3508))  # A4 size vertical
        print("Resized Dimensions: " + str(img), resizedImage.shape)
        cv2.imwrite("PhotoMosaicColorResized.jpg", resizedImage)
        print("Done!")
        quit()

cv2.destroyAllWindows()

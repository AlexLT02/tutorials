# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color

img_normal = cv2.imread('./tutorials/data/images/sift_table05.jpg', cv2.IMREAD_UNCHANGED)
img_gray = cv2.imread('./tutorials/data/images/sift_table05.jpg', cv2.IMREAD_GRAYSCALE)

# TODO Do some print out about the loaded data using type, dtype and shape
print(type(img_normal))
print(type(img_gray))


# TODO Continue with the grayscale image
img = img_gray.copy()

# TODO Extract the size or resolution of the image


# TODO Resize image

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row

# TODO Print first column

# TODO Continue with the color image

# TODO Set an area of the image to black

# TODO Show the image and wait until key pressed

# TODO Find all used colors in the image

# TODO Copy one part of an image into another one

# TODO Save image to a file

# TODO Show the image again

# TODO Show the original image (copy demo)

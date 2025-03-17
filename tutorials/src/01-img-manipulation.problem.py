# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

# TODO First step is to import the opencv module which is called 'cv2'
import cv2

# TODO Check the opencv version
print(cv2.__version__)

# TODO Load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.
img_unchanched = cv2.imread('./tutorials/data/images/sift_table05.jpg', cv2.IMREAD_UNCHANGED )

# TODO Resize image with 'resize'
new_hight = 400
new_width = 800
newSize = (new_width, new_hight)
img = cv2.resize(img_unchanched, newSize)

# TODO Rotate image (but keep it rectangular) with 'rotate'

img = cv2.rotate(img, cv2.ROTATE_180)

# TODO Save image with 'imwrite'

cv2.imwrite('img_tutorial01.jpg', img)

# TODO Show the image with 'imshow'
cv2.imshow('tutorial01.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


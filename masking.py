import cv2 as cv
from rescaleImage import rescaleImage
import numpy as np


oldimg = cv.imread("images/third.png")
img = rescaleImage(oldimg, 0.4)

# img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", img2)

blank = np.zeros(img.shape[:2], dtype="uint8")


blank2 = np.zeros((img.shape[0], img.shape[1], 3), dtype="uint8")
blank2[:] =(0,0,255)

# cv.imshow("blank2", blank2)

mask = cv.circle(blank, (img.shape[1]//2 + 10, img.shape[0]//2 + 80), 150, 255, -1)
# cv.imshow("Mask", mask)
mask_inv = cv.bitwise_not(mask)

img_part = cv.bitwise_and(img, img, mask=mask)
cv.imshow("img", img_part)
red_part = cv.bitwise_and(blank2, blank2, mask=mask_inv)
cv.imshow("red", red_part)

results = cv.add(img_part, red_part)
cv.imshow("new image", results)


# masking allows us to focus on the certain part of the image, 
# masked = cv.bitwise_and(blank2, img, mask=mask_inv)
# cv.imshow('Masked img', masked)

cv.waitKey(0)
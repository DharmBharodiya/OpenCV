import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# outside of OpenCV we use RGB color space format


img = cv.imread("images/second.jpg")

def rescaleImage(img, scale=0.20):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

newImg = rescaleImage(img)

#BGR -> normal colors

# BGR to GrayScale
gray = cv.cvtColor(newImg, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR to HSV (Hue saturation value)
# based on how humans think and concieve colors
hsv = cv.cvtColor(newImg, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b -> looks like the washed down version of the BGR image
lab = cv.cvtColor(newImg, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(newImg, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv 2 bgr", hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow("lab 2 bgr", lab_bgr)

# grayscale cannot directly be converted to hsv, it needs to be mediated by conversion to bgr first

#defualt of matplotlib is rgb while for opencv is bgr
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
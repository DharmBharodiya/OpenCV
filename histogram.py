import cv2 as cv
from rescaleImage import rescaleImage
import numpy as np
import matplotlib.pyplot as plt

# histogram is basically the representation of pixel intensities (brightness values) in an image
# for a grayscale image - it shows how may pixels have each intensity value 
# for a color image - you get separate histograms for ech channel

oldimg = cv.imread("images/third.png")
img = rescaleImage(oldimg, 0.4)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# grayscale histogram
#syntax -> (images, channels, mask, histSize->no of bins, ranges->pixel value range)
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

#bins -> like a bucket that groups pixels value together
# when creating histogram, we are counting how many pixels fall into each bin - that is how many pixesl have values within a certain range
# list of images, no. of channels, mask, histSize -> bins, range of all possible pixel values
plt.figure()
# ex. bin -> [256] -> number of bins = 256 (eac intensity has its own bin)
plt.title("grayscale histogram")
plt.xlabel("bins")
plt.ylabel("no. of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)
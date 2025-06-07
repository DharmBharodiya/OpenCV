import cv2 as cv
from rescaleImage import rescaleImage
import numpy as np

# thresholding is basically used to segment an image
# if a pixel value is above a certain threshold, make it white
# if it is below, than make it black

# this gives you a binary image, which is perfect for detecting shapes

#syntax
# retval, thresholded_image = cv.threshold(src, thresh, maxval, type)
# here retval, or return value, is basically the actual threshold value that the function used to create an image
# maxval is the maximum value
# thresh is the threshold value
# type is the type of thresholding we want to have, ex. THRESH_BINARY, THRESH_BINARY_INV

oldimg = cv.imread("images/third.png")
img = rescaleImage(oldimg, 0.4)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# simple thresholding
# to apply this we use cv.threshold funcction
# this function returns threshold and thresh
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple threshold", thresh)

# inverse thresholding
threshold, threshold_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple threshold inverse", threshold_inv)

# syntax
# thresholded_image = cv.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# src: Source grayscale image
# maxValue: The value to assign to pixels exceeding the threshold (usually 255)
# adaptiveMethod: The algorithm to calculate the threshold for a pixel (e.g., cv.ADAPTIVE_THRESH_MEAN_C, cv.ADAPTIVE_THRESH_GAUSSIAN_C)
# thresholdType: The type of thresholding (e.g., cv.THRESH_BINARY, cv.THRESH_BINARY_INV)
# blockSize: Size of a pixel neighborhood that is used to calculate the threshold value (must be odd, e.g., 11, 15), size of kernel
# C: A constant subtracted from the mean or weighted mean (fine-tunes the thresholding)

# adaptive thresholding
# in other type of thresholding we werer specifying the thresholding value
# but in adaptive one, we let the computer comuputer the best value for the thresholding

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adapative thresholding", adaptive_threshold)

cv.waitKey(0)
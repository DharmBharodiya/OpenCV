import cv2 as cv
from rescaleImage import rescaleImage
import numpy as np

oldimg = cv.imread("images/third.png")
img = rescaleImage(oldimg, 0.4)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# these are both gradient based methods 

#laplacian -> finds edges in all directions, internsity change rate, second derivative
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)
# syntax
# laplacian_image = cv.Laplacian(src, ddepth, ksize)
# src: Source image (should be in grayscale for edge detection)
# ddepth: Desired depth of the destination image (e.g., cv.CV_64F for floating point output)
# ksize: Aperture size used to compute the second-derivative filters (must be odd and positive, e.g., 1, 3, 5)

# sobel -> finds eges in specific directions, first derivative
# computes gradients in two direction, x and y
#Sobel uses first-order derivatives to calculate the rate of change in pixel intensity. It highlights regions where intensity changes sharply — that is, edges.

# It does this separately in the horizontal (X) and vertical (Y) directions.

#synat
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel x', sobelx)
cv.imshow("Sobel y", sobely)
cv.imshow("combined", combined_sobel)
# syntax
# sobel_image = cv.Sobel(src, ddepth, dx, dy, ksize)
# src: Source image (should be in grayscale for edge detection)
# ddepth: Desired depth of the destination image (e.g., cv.CV_64F for floating point output)
# dx: Order of the derivative in x direction (1 for x-derivative, 0 otherwise)
# dy: Order of the derivative in y direction (1 for y-derivative, 0 otherwise)
# ksize: Size of the extended Sobel kernel; must be 1, 3, 5, or 7


canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)
cv.waitKey(0)
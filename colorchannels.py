import cv2 as cv
import numpy as np
from rescaleImage import rescaleImage 

img = cv.imread("images/third.png")
newImg = rescaleImage(img, 0.4)
# cv.imshow("resized image", newImg)

blank = np.zeros(newImg.shape[:2], dtype="uint8")

b,g,r = cv.split(newImg)
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank, blank, r])
cv.imshow("blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

# print(newImg.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

#in each of these images, we can observe that for the areas that are lighter in color, it means that, that area is densed with the pixels of that color and the darker or ore black color means the absence of those colors

# merged = cv.merge([b,g,r])
# cv.imshow('merged', merged)

cv.waitKey(0)
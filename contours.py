import cv2 as cv
import numpy as np

#contours -> basically the boundaries of object, the line or curve that joins objects -> used in shape analysis, detection and etc

img = cv.imread("images/second.jpg")



def rescaleImage(img, scale=0.20):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

newImg = rescaleImage(img)
blank = np.zeros(newImg.shape, dtype="uint8")
cv.imshow("blank", blank)
#[:2] is basically slicing, .shape method returns a tuple havonh(height, width, channels), and here :2 means we sliced to the first two eles of the tuples, height and width
# i.e; we just gave the height and width of the newImg as the dimensions of out blank image

gray = cv.cvtColor(newImg, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blurring the img would significanltly reduce the size of contours
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(blur, 125,175)
cv.imshow('Cannny', canny)

#other method to find contours is to using thresholds
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# thresholding basically looks at an image and tries to binarize an image(to divide it into two white and black)
# if the intensity of the pixel is less than 125 it makes it black, and if it is more than 255 it makes it white
cv.imshow("Threshold", thresh)
#to find contours
# returns -> contours, and heirarchies
contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# cv.findcontours looks for the edges in the image, and return contours which is the list of all the coordinates of the contours found in the image,
# heirarchies referes to the heirarchial represntation of the contours, like rectangle, inside which is a circle inside it square, etc
#cv.RETR_LIST -> essentially is a mod in which find contours methods is written, LIST returns all the contours, RETR_EXTERNAL -> only returns the extrenal or outter contours, RETR_TREE -> returns all the heirarchial contours
# contour approx method -> how we want to approx the contours, CHAIN+APPROX_NONe basically returns all the contours, APPROC_SIMPLE -> essentialy takes all the contours the points and simplifies it to with just two points to make a line with

cv.drawContours(blank, contours, -1, (0,0,255), 1)
# blank -> where to draw, contours -> the list to draw contours from, -1 -> means to draw all the contours, (0,0,255) makes it of red color, 2 is the thickness
cv.imshow("Drawn contours", blank)

print(f'{len(contours) }contour(s) found')

# cv.imshow("Image", img)

cv.waitKey(0)
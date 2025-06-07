import cv2 as cv
import numpy as np

#tow ways to draw on an image, by actually drawing on the standalone image like as we passed in the img
# or by creating a blank image(dummy) and then drawing on it

# here the np.zeros is used to create a blank image
# it takes two arguments, the height and widht of the image
# and dtype is the data type of the image, her uint8 it is which means 8 bit unsigned integer and it refers to the range of values that can be stored in the image

blank = np.zeros((500,500,3), dtype="uint8") # the 3 here means the number of channels in the images, here it is 3 because it is a color image which means red green and blue channels
# cv.imshow('Blank Image', blank)

# 1. Paint the image a certain color
# blank[:] = 0,0,255 # this will paint the image a certain color, here blue
# the [:] means all the pixels in the image
# cv.imshow('blue', blank)


# to have only certain pixesl of the image to be of certain color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)
# here the 200:300 means the rows and the 300:400 means the columns

# 2. draw a rectangle
# cv.rectangle(blank, (0,0), (250, 500), (0,255,0), thickness=2)#here (0,0) is the starting point and (250, 500) is the ending point#
# or you can have thickness = cv.filled or -1 to have the area filled with the color
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),  (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)



# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=4) # here the 40 is the radius of the circle
cv.imshow('Circle', blank)


#4. Draw a line
cv.line(blank, (blank.shape[1],0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)




# img =cv.imread('images/second.jpg')

# cv.imshow('Second Image', img)



cv.waitKey(0)
import cv2 as cv

#to read an image , this method takes an images and returns it as an matrix of pixels
img = cv.imread('images/first.jpg')#image is referenced relatively here as it is in the same directory, 

#now to  display the image using cv.imshow method
cv.imshow('First Image', img)
#this method takes two argument, the window name and the image to be displayed

#this method waits for a key to be pressed. as it is 0, it will wait for an infinite time
cv.waitKey(0)




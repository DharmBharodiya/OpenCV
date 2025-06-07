import cv2 as cv

img = cv.imread('images/first.jpg')

#this method would work on images, videos and live videos
def rescaleImage(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(image, dimension, interpolation=cv.INTER_AREA)

resized_image = rescaleImage(img, 0.5)
cv.imshow('First Image', img)
cv.imshow('Resized Image', resized_image)

cv.waitKey(0)
cv.destroyAllWindows()
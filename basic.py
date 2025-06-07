import cv2 as cv

img = cv.imread("images/second.jpg")
# cv.imshow("Image", img)

def rescaleImage(image, scale=0.10):
    width = int(image.shape[1] * scale);
    height = int(image.shape[0] * scale);
    dimensions = (width, height);

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

resizedImage = rescaleImage(img)
#converting to grayscale
gray = cv.cvtColor(resizedImage, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur
blur = cv.GaussianBlur(resizedImage, (3,3), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

#edge cascase - to find out the edges present in the image
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny", canny)

# dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)

#cropping 
cropped = img[50:200,200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
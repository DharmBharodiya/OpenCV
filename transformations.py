import cv2 as cv
import numpy as np

img = cv.imread("images/third.png")

#translating
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
# x --> Right
# y --> Down  

translated = translate(img, 100, 100)
cv.imshow("Translate", translated)


resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_CUBIC);
cv.imshow("resized", resized)

flip = cv.flip(resized, -1)
# 0 --> vertical flip
# 1 --> horizontal flip
# -1 --> flippig both ways
cv.imshow("Flip", flip)

cropped = img[200:400, 300:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
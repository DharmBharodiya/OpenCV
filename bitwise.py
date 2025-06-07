import cv2 as cv
import numpy as np

# bitwise operations work at pixel level, and performs logical operations like
# AND, OR, XOR, NOT
# each pixel has a color value (0 to 255) and bitwise ops treat values as binary and then apply logical rules
# it could be helpful in masking, cutting out a shape from an image, merging two images, removing or keeping backgrounds 
# pixel on if it is 1 and off if it is 0


blank = np.zeros((400,400), dtype="uint8");
 # we will draw a rect and circle on the blank image

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
# img, start pos, end pos, color, thickness -> -1 to fill

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rect", rectangle)
cv.imshow("circle", circle)

# bitwise AND -> what this does is it basically gets the intersection of two images, or we can say it only keeps the things which are common to both the images
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwiseAnd)

# bitwise OR -> what this does is it gives eveything by combining both the images, both intersecting and non-intersecting
bitwiseOr = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwiseOr)

# bitwise XOR -> gives non-intersecting regions, basically birtwise or - bitwise and
bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow("BItwise XOR", bitwiseXor)

# bitwise not -> doesnt returns anything just inverts binary color
bitwiseNot = cv.bitwise_not(rectangle)
cv.imshow("Bitwise Not", bitwiseNot)

cv.waitKey(0)
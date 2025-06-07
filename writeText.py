import cv2 as cv
import numpy as np

blank = np.zeros((600, 600, 3), dtype="uint8")

cv.putText(blank, 'Dharm', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow("Text", blank)

cv.waitKey(0)
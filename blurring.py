import cv2 as cv
from rescaleImage import rescaleImage

oldimg = cv.imread("images/third.png")
img = rescaleImage(oldimg, 0.4)

# cv.imshow("resize image", img)

# while blurring we have to describe a kernel
# a kernel is a window that we draw over a specific portion of the image
# the size of the window/ or the size of the kernel is basically the no. of rows and no. of columns

# now there are several methods through which blur can be applied to the image
# the first is like if we have 3X3 kernel, then the blur happens in the center piece [2,2] as a result of the othe surrounding pieces

# averaging
# here the new pixel internsity of the particular region would be the average of the surrounding pixels
# this process is done for the whole image by moving the window in horizontal and vertical directions throughout the image

# more kernel size -> more blur
average = cv.blur(img, (3,3))
cv.imshow("Avg blur", average)

# gaussian blur -> basically same as averaging, but instead of averaging surrouding pixels, it gives weight to all the surrounding pixels, and the average of product of the weight gives the new intensity
# here we get less blur than the average one, but this blur is much natural comparatively
gauss = cv.GaussianBlur(img, (3,3), 0) # the third arg is sigmaX or std. deviation in direction x
cv.imshow("gauss blur", gauss)

# median blur -> also same as averaging, but instead of finding average of surrounding pixels, here we find median of the surrounding pixels
# good for reduccing noise in image, pretty good in removing salt and pepper noise, 
median = cv.medianBlur(img, 3) #here opencv assumes that kernel size is 3X3 no need to pass tuple
cv.imshow("median blur", img)
# not meant fr high kernel sizes like even 5 or 7, etc

# bilateral blurring -> most effective, used in adv. cmpter vision programs
# here blur is applied but also retains the edges which is not the case in other types of blurring
bilateral = cv.bilateralFilter(img, 20, 35, 25)
# 5 is the diameter of pixel neighborhood
# third arg is sigmacolor which is basially the range of colors to be considered for blur
# 4th is sigmaspace -> larger values means farther pixels was also influence the blur
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
#rescaling an image means to change the height and width of the image to a particular value
import cv2 as cv

# img = cv.imread('images/first.jpg')
# cv.imshow('First Image', img)

#now to rescale the image, we need to divide the height and width by a particular value
#we can do this by using the resize method
#this method takes two arguments, the width and height of the image
#we can also use the scale factor to rescale the image
#the scale factor is the factor by which the image is to be rescaled
#we can use the scale factor to rescale the image

#works for images, videos and live videos
def rescaleFrame(frame, scale=0.75): #frame is the image to be rescaled and scale is the factor by which the image is to be rescaled
    width = int(frame.shape[1] * scale);#[0] means the height of the image and [1] means the width of the image
    height = int(frame.shape[0] * scale);
    dimensions = (width, height)# here we have widht and height as a tuple

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)#this method actually resizes the image acc to the dimensions we have provided
    # the interpolation is the method by which the image is to be resized
    #INTER_AREA means the area of the images is to be preserved, which in simple word means that the image is to be resized without distortion

# works for live videos
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
# the changeRes function is used to change the resolution of the video
# the 3 and 4 are the width and height of the video
# similary with this kind of indices, like 10 we can change the brightness, contrast, saturation, etc.
# those indices are called properties of the video
# indices are as follows: 3 is width, 4 is height, 10 is brightness, 11 is contrast, 12 is saturation, 13 is hue, 14 is gain, 15 is gamma, 16 is exposure, 17 is sharpness, 18 is color temperature, 19 is white balance, 20 is focus, 21 is focus area, 22 is focus mode, 23 is focus distance, 24 is focus metering, 25 is focus priority, 26 is focus area, 27 is focus mode, 28 is focus distance, 29 is focus metering, 30 is focus priority

capture = cv.VideoCapture('videos/firstVideo.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.30)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

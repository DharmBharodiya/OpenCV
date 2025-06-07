import cv2 as cv

#reading a video
capture = cv.VideoCapture('videos/firstVideo.mp4')
#the way we read videos is by using the VideoCapture method
#this method takes the path of the video as an argument
# or it takes the index of the camera as an argument
# like webcam referenced as 0, 1 would be 1st camera connected and 2 would be 2nd camera connected and so on

# it is a bit different from reading an image
# we read the video frame by frame
# we use while loop to read the video frame by frame
# we use read method to read the video frame by frame
# we use imshow method to display the video frame by frame
# we use waitKey method to wait for a key to be pressed
# we use destroyAllWindows method to destroy all windows
# we use release method to release the video capture

while True:
    isTrue, frame = capture.read()#this capture.read method reads the video frame by frame and it returns two values, istrue and frame, so the boolean says if the frame is read successfully and frame is the actual frame

    cv.imshow('Video', frame)#this imshow method displays the video frame by frame

    #to stop video from playing indefinitely,
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()# here release method means to stop the video from playing
cv.destroyAllWindows()# destroyAllWindows means to close all the active windows

# assestion -215 error means that the end to frames was reached or the video was not found
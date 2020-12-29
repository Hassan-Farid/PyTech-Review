import cv2
import sys
import numpy as np

#Creating a video capture object
cap = cv2.VideoCapture(0) #0 represents first camera. For multiple cameras use the specific number on which to display image

#Checking if the camera is open to capture video
if cap.isOpened() == 0:
    sys.exit("Camera could not be opened")

#Capturing video frame-by-frame
while (True):
    ret, frame = cap.read() #Returns a tuple of (ret, frame). Ret contains boolean value specifying whether next frame can be loaded or not
    print(ret)
    print(frame)
    
    #Terminate program if stream gets broken
    if not ret:
        print("Could not retrieve frame from the capture object... Terminating Stream")
        break
    
    #Displaying each video frame as grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Converts BGR format to GRAYSCALE format
    
    #Displaying the video captured frame-by-frame
    cv2.imshow('Video Frames', gray)
    
    #Terminate the video capture object if key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#Releasing capture once done with the video display
cap.release()

#Destroying all GUI Image Windows
cv2.destroyAllWindows()
    
    
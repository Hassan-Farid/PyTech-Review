import cv2
import sys
import numpy as np

#Creating video capture object for specified video
cap = cv2.VideoCapture('./Videos/sample.mp4')

#Saving the Gray Scale version of the Video
fourcc = cv2.VideoWriter_fourcc(*'XVID') #Creates a codec for AVI format videos
out = cv2.VideoWriter('./Videos/grey_sample.avi', fourcc, 29.97, (1280,720)) #Creates a video object with 29.97 fps and (1280, 720) frame size

#Creating a Gray Scale version of the video
while (cap.isOpened()): #Keeps displaying frames until video is finished
    
    ret, frame = cap.read()
    
    #Checking if the next frame is available or not
    if not ret:
        print("Could not find next frame.... Terminating stream")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Writing frame to the video to be saved
    out.write(gray)
    
    cv2.imshow('Gray Frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #Terminate display if 'q' key is pressed
        break
    
#Releasing the video capture objects
cap.release()
out.release()

#Destroying all windows
cv2.destroyAllWindows()


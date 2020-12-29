import cv2
import sys
import numpy as np

#Creating video capture object
cap = cv2.VideoCapture(0)

#Getting video capture properties (Using 0-18 property identifiers as indicated below)
ret, frame = cap.read()

#Accessing properties using get() method. Only usually used properties are mentioned
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #Width of each frame
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #Height of each frame
print(cap.get(cv2.CAP_PROP_FPS)) #Getting frame rate of each frame
print(cap.get(cv2.CAP_PROP_BRIGHTNESS)) #Get brightness of the frame
print(cap.get(cv2.CAP_PROP_CONTRAST)) #Get contrast of the frame
print(cap.get(cv2.CAP_PROP_SATURATION)) #Gets saturation of the frame
print(cap.get(cv2.CAP_PROP_GAIN)) #Gets gain of the frame
print(cap.get(cv2.CAP_PROP_HUE)) #Gets hue of the frame
print(cap.get(cv2.CAP_PROP_EXPOSURE)) #Gets exposure of the frame
print("=============================================")
print("=============================================")

cv2.imshow('Video Frame', frame)
cv2.waitKey(0)

#Now setting these properties so as to change the video capturing using set() method
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720.0) #Width of each frame
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 560.0) #Height of each frame
cap.set(cv2.CAP_PROP_FPS, 60.0) #Setting frame rate of each frame
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.0) #Set brightness of the frame
cap.set(cv2.CAP_PROP_CONTRAST, 16.0) #Set contrast of the frame
cap.set(cv2.CAP_PROP_SATURATION, 32.0) #Sets saturation of the frame
cap.set(cv2.CAP_PROP_GAIN, 1.0) #Sets gain of the frame
cap.set(cv2.CAP_PROP_HUE, 1.0) #Sets hue of the frame
cap.set(cv2.CAP_PROP_EXPOSURE, 1.0) #Sets exposure of the frame

#Accessing the capture object after altering values for the frame
ret, frame = cap.read()

cv2.imshow('New Video Frame', frame)
cv2.waitKey(0)

#Releasing the capture object
cap.release()

#Destroying all opened windows
cv2.destroyAllWindows()  
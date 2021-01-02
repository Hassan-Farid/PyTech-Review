import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/A.jpg')

#Converting read image into Grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Applying threshold on the image such that all values below 127 are turned to 0 whereas others turn to 1
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

#Configuring settings for finding contours from the object
mode = cv2.RETR_TREE
method = cv2.CHAIN_APPROX_SIMPLE

#Finding the contours from the image
contours, hierarchy = cv2.findContours(thresh, mode, method)

#Displaying the list of contours found from the image
for x in contours:
    print(x)
    print("--------------")
    
#Displaying hierarchy of the contours
print(hierarchy)
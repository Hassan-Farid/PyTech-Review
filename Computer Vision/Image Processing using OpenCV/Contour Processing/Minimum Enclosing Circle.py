import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/electric.jpg')
new_img = img.copy()

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating thresholded image
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

#Finding contours from the image
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing minimum enclosing circle for the image and drawing it to the image
for c in cnts:
    (x,y), radius = cv2.minEnclosingCircle(c) #Getting the center and radius to create minimum enclosing circle for the image
    center = (int(x), int(y)) #Converting centers from floats to integers just in case
    radius = int(radius) #Converting radius from floats to integers just in case
    new_img = cv2.circle(new_img, center, radius, (0,255,0), 1) #Drawing minimum enclosing circle on the image
    
#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Minimum Enclosed Circle Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

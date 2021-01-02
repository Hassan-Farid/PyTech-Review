import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/electric.jpg')
new_img = img.copy()

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Computing thresholded image
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

#Finding contour points from the image
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing the fitted ellipse for the image and drawing it to the image
for c in cnts:
    if len(c) >= 5: #Since an ellipse can be fitted on only those contours with at least 5 points
        ellipse = cv2.fitEllipse(c) #Creating a fitted ellipse (contains all the properties of ellipse such as center, axeslength, startAngle, etc)
        new_img = cv2.ellipse(new_img, ellipse, (0,255,0), 2) #Using the fitted ellipse to create an ellipse on the image
    
#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Fitted Ellipse Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np


#Reading image from the Images folder
img = cv2.imread("./Images/hands.jpg")
new_img = img.copy()

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Computing threshold for the image
ret, thresh = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

#Finding contours from the image
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Configuring settings for computing convex hull of the image
orient = False #Anti-clockwise orientation
returnPoints = True #Provides the coordinates of hull points (For False, gives the corresponding contour points)

#Computing hull points of the image and displaying them in another window
for c in cnts:
    hull = cv2.convexHull(c, None, orient, returnPoints)
    cv2.drawContours(new_img, [hull], -1, (0,255,0), 2)

#Displaying the images on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Convex Hull Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
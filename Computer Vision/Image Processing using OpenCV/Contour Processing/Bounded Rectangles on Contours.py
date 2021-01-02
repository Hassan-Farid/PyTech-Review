import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/electric.jpg')
img1 = img.copy()
img2 = img.copy()

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Finding thresholded Image
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

#Finding contours from the image
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Creating a bounded rectangle on the contour (Not the minimum enclosing)
for c in cnts:
    x, y, w, h = cv2.boundingRect(c) #Getting the top-left (x,y) coordinate and width and hegiht of rectangle 
    img1 = cv2.rectangle(img1, (x,y), (x+w, y+h), (0,255,0), 1) #Drawing rectangle on the image

#Creating a bounded rotated rectangle on the contour (Minimum enclosing)
for c in cnts:
    minArea = cv2.minAreaRect(c) #Computing the minimum enclosing area
    box = np.int0(cv2.boxPoints(minArea)) #Creating a rectangle from the minimum enclosing area
    img2 = cv2.drawContours(img2, [box], -1, (0,0,255), 1) #Drawing rectangle based contours on the image

#Displaying image on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Bounded Rectangle', img1)
cv2.imshow('Minimum Enclosing Rectangle', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
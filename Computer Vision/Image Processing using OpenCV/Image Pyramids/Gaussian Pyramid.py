import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread("./Images/image1.jpg")

#Creating lower resolution images using Gaussian Image Pyramids
lower1 = cv2.pyrDown(img)
lower2 = cv2.pyrDown(lower1)

#Reincreasing the resolution of the images using Gaussian Image Pyramid
upper1 = cv2.pyrUp(lower2)
upper2 = cv2.pyrUp(upper1)

#Displaying images 
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Pyramid Level 1', lower1)
cv2.imshow('Gaussian Pyramid Level 2', lower2)
cv2.imshow('Gaussian Pyramid Undo Level 2', upper1)
cv2.imshow('Gaussian Pyramid Undo Level 1', upper2)

cv2.waitKey(0)
cv2.destroyAllWindows()
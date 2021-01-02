import cv2 
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\detected_ball.jpg')

#Configuring settings for the median blurring
ksize = 7

#Applying median blur
median = cv2.medianBlur(img, ksize)

#Displaying images on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Median Blur Image', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
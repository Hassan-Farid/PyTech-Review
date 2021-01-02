import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\grid.jpg')

#Configuring settings for applying Scharr gradient
ksize = -1
ddepth = -1

#Applying scharr gradient on the image
x_sobel = cv2.Sobel(img, ddepth, dx=1, dy=0, ksize=ksize)
y_sobel = cv2.Sobel(img, ddepth, dx=0, dy=1, ksize=ksize)

#Displaying images on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Horizontal Scharr Gradient', x_sobel)
cv2.imshow('Vertical Scharr Gradient', y_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
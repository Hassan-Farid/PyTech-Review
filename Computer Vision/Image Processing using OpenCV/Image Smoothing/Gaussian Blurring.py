import cv2
import numpy as np

#Reading the image from the Images folder
img = cv2.imread(".\Images\detected_ball.jpg")

#Configuring settings for the Gaussian Blurring
ksize = (7,7) #Kernel size
stdx = 0 #Standard deviation along x-axis
stdy = 0 #Standard deviation along y-axis

#Applying Gaussian Blur to the image
gauss = cv2.GaussianBlur(img, ksize, sigmaX=stdx, sigmaY=stdy)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blur Image', gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

#Reading image from the images folder
img = cv2.imread(".\Images\soccerball.jpg")

#Resizing the image using different interpolations

#Configuring settings for the resizing of image
fx = 2 #Resizing along the x-axis
fy = 2 #Resizing along the y-axis
dsize = None

#Expanding an image (Cubic is slower but gives faster result)
cubic_expand = cv2.resize(img, dsize=dsize, fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
linear_expand = cv2.resize(img, dsize=dsize, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

#Shrinking an image
area_shrink = cv2.resize(img, dsize=dsize, fx=1/fx, fy=1/fy, interpolation=cv2.INTER_AREA)
linear_shrink = cv2.resize(img, dsize=dsize, fx=1/fx, fy=1/fy, interpolation=cv2.INTER_LINEAR)

#Displaying the images
cv2.imshow('ORIGINAL Image', img)
cv2.imshow('CUBIC EXPAND Image', cubic_expand)
cv2.imshow('LINEAR EXPAND Image', linear_expand)
cv2.imshow('AREA SHRINK Image', area_shrink)
cv2.imshow('LINEAR SHRINK Image', linear_shrink)

cv2.waitKey(0)
cv2.destroyAllWindows()
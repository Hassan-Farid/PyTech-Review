import cv2
import numpy as np

#Reading image from the Images folder (We use the image we extracted by applying color based object detection)
img = cv2.imread('.\Images\detected_ball.jpg')

#Configuring settings for applying Average Blurring
ksize = (7,7) #Kernel size

#Applying average blurring
blur = cv2.blur(img, ksize) #Using blur() method
boxfilter = cv2.boxFilter(img, -1, (5,5)) #Using boxFilter() method

#Displaying the image
cv2.imshow('Original Image', img)
cv2.imshow('Blur Filter Image', blur)
cv2.imshow('Box Filter Image', boxfilter)

cv2.waitKey(0)
cv2.destroyAllWindows()
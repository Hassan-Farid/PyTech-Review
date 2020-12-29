import cv2
import numpy as np

#Reading two different images from the Images folder
img1 = cv2.imread('.\Images\image3.jpg')
img2 = cv2.imread('.\Images\image4.jpg')

#Blending these images into a single image using Linear Blending (Weighted Sum of ndarrays)
alpha = 0.4 #Transparency of first image
beta = 1 - alpha #Transparency of second image
gamma = 0 #Scalar added to the resultant image

#One constraint of adding images is that the images should have equal dimensions as well as datatype
img = cv2.addWeighted(img2, alpha, img1, beta, gamma)

#Displaying the added images and individual images on the screen
cv2.imshow('First image', img1)
cv2.waitKey(0)

cv2.imshow('Second image', img2)
cv2.waitKey(0)

cv2.imshow('Added Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
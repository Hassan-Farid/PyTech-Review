import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\dotted_A.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for applying TopHat Transform
ksize = 5
kernel = np.ones((ksize, ksize), np.uint8)
op = cv2.MORPH_TOPHAT

#Applying the TopHat Transform on the image
top_img = cv2.morphologyEx(img, op, kernel)

#Displaying the images
cv2.imshow('Original Images', img)
cv2.imshow('Top Hat Transform Image', top_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
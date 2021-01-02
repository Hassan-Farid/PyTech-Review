import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\holes_A.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for the Close Transform
ksize = 5
kernel = np.ones((ksize, ksize), np.uint8)
op = cv2.MORPH_CLOSE
iters = 2

#Applying close transform to the image
close_img = cv2.morphologyEx(img, op, kernel, iterations=iters)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Clost Transform Image', close_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
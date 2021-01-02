import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\dotted_A.jpg', cv2.IMREAD_GRAYSCALE)

#Setting configuration to apply Opening Transform
ksize = 5 #Size of kernel
kernel = np.ones((ksize, ksize), np.uint8) #Creating array of neighbourhood pixels for a certain pixel
op = cv2.MORPH_OPEN #Type of morphological transform being applied
iters = 2 #Number of times open transform is to be applied

#Applying open transform to the image
open_img = cv2.morphologyEx(img, op, kernel, iterations=iters)

#Displaying images 
cv2.imshow('Original Image', img)
cv2.imshow('Open Transform Image', open_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
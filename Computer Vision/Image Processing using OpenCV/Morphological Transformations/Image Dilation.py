import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\A.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for applying Dilation effect
ksize = 5 #Size of kernel
kernel = np.ones((ksize, ksize), np.uint8) #Creating array of neighbourhood pixels of each pixel
iters = 2 #Number of times dilation is to be applied

#Applying dilation on the provided image
#Dilation is the opposite process of Erosion
#Dilaion selects the maximum pixel value within the neighbourhood of a pixel and assigns it to that pixel thus dialating the less pixel values
dilated = cv2.dilate(img, kernel, iterations=iters)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Dilated Image', dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
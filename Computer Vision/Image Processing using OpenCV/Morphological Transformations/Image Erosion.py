import cv2
import numpy as np

#Reading image from the Images folder (Use Grayscale Format)
img = cv2.imread('.\Images\A.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for applying erosion on the image 
ksize = 5 #Size of kernel 
kernel = np.ones((ksize, ksize), np.uint8) #Creating a array of pixels within the neighbourhood of a pixel
iters = 2 #Number of times erosion is to be applied

#Applying erosion on the provided image
#Erosion selects the minimum pixel value within the neighbourhood of a pixel and assigns it to that pixel thus eroding the greater pixel values
eroded = cv2.erode(img, kernel, iterations=iters) 

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Eroded Image', eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread(".\Images\cricketballs.jpg")

#Converting image into grayscale to apply adaptive thresholding
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Configuring the values for applying adaptive thresholding
thresh_type = cv2.THRESH_BINARY #We apply the binary thresholding as threshold type for adaptive thresholding
blocksize = 5 #Number of pixels in the neighbourhood of the pixel on which the adaption is to be applied
const = 1 #A constant value to be subtracted from the value obtained using the adaptive thresholding
maxval = 255

#Applying Mean Adaptive Thresholding
mean_thresh = cv2.adaptiveThreshold(img, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, thresh_type, blocksize, const)

#Applying Gaussian Adaptive Thresholding
gauss_thresh = cv2.adaptiveThreshold(img, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresh_type, blocksize, const)
 
#Displaying images on the screen
cv2.imshow('GRAYSCALE Image', img)
cv2.imshow('MEAN ADAPTIVE THRESHOLD', mean_thresh)
cv2.imshow('GAUSSIAN ADAPTIVE THRESHOLD', gauss_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
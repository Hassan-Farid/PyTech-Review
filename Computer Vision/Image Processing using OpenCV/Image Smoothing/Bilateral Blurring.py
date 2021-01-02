import cv2
import numpy as np
import sys

#Reading image from the Images folder
img = cv2.imread("./Images/plate.jpg")

if img is None:
    sys.exit("Image could not be found at specified folder")
    
#Creating named windows
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Bilateral Filtered Image', cv2.WINDOW_NORMAL)
    
#Configuring settings for applying a bilateral filter
d = 10 #Size of pixel neighbourhood on which filter is to be applied
scolor = 350 #Value to determine extent of color mixture by filter
sspace = 350 #Value to determine extent of influence of pixels on each other if color values are approximate 

#Applying bilateral filter on the image
bilateral = cv2.bilateralFilter(img, d, scolor, sspace)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Bilateral Filtered Image', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
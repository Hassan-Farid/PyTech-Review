import cv2
import numpy as np

#Reading the image from the screen
img = cv2.imread(".\Images\image3.jpg", cv2.IMREAD_GRAYSCALE)

#Configuring settings for applying Canny Edge Detection on the Image
minval = 100
maxval = 200
ksize = 3 
gradval = True

#Applying Canny Edge Detection on the image
canny = cv2.Canny(img, minval, maxval, apertureSize=ksize, L2gradient=gradval)

#Displaying the image
cv2.imshow('Original Image', img)
cv2.imshow('Canny Detected Image', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

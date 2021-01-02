import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/grid.jpg')

#Configuring settings for applying Laplace Derivative/Gradient
ksize = 3
ddepth = -1

#Applying Laplacian/Laplace Gradient on the image
laplace = cv2.Laplacian(img, ddepth, ksize=ksize)

#Displaying image on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Laplacian Image', laplace)

cv2.waitKey(0)
cv2.destroyAllWindows()
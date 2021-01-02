import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/image1.jpg')

#Creating Gaussian Pyramid Levels for the image
print(img.shape)
lower1 = cv2.pyrDown(img) #Represents level 1
print(lower1.shape)
lower2 = cv2.pyrDown(lower1) #Represents level 2
print(lower2.shape)
upper1 = cv2.pyrUp(lower2) #Represents level 1 resoluted
print(upper1.shape)
upper2 = cv2.pyrUp(upper1) #Represents level 0 resoluted
print(upper2.shape)

#Computing Laplace Pyramid using the difference of the above mentioned Gaussian Pyramids
laplace1 = cv2.subtract(lower1, upper1)
#laplace2 = cv2.subtract(img, upper2)

#Displaying the image
cv2.imshow('Original Image', img)
cv2.imshow('Laplacian Pyramid Level 1', laplace1)
#cv2.imshow('Laplacian Pyramid Image', laplace2)

cv2.waitKey(0)
cv2.destroyAllWindows()
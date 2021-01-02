import cv2
import numpy as np

#Reading image from the Images folder
rect_img = cv2.imread('./Images/rect.jpg', cv2.IMREAD_GRAYSCALE)
ellipse_img = cv2.imread('./Images/ellipse.jpg', cv2.IMREAD_GRAYSCALE)
cross_img = cv2.imread('./Images/cross.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for the structuring elements
ksize = (5,5) 

#Creating structuring element for rectangle shape
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)

#Creating structuring element for ellipse shape
ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)

#Creating structuring element for circle shape
circle_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, ksize)

#Applying kernels using various morph transforms
gradient_rect = cv2.morphologyEx(rect_img, cv2.MORPH_GRADIENT, rect_kernel)
gradient_ellipse = cv2.morphologyEx(ellipse_img, cv2.MORPH_GRADIENT, ellipse_kernel)
gradient_cross = cv2.morphologyEx(cross_img, cv2.MORPH_GRADIENT, circle_kernel)

#Displaying the images
cv2.imshow('Rectangle', rect_img)
cv2.imshow('Eroded Rectangle', gradient_rect)
cv2.waitKey(0)

cv2.imshow('Ellipse', ellipse_img)
cv2.imshow('Dilated Ellipse', gradient_ellipse)
cv2.waitKey(0)

cv2.imshow('Circle', cross_img)
cv2.imshow('Gradient Circle', gradient_cross)
cv2.waitKey(0)

cv2.destroyAllWindows()
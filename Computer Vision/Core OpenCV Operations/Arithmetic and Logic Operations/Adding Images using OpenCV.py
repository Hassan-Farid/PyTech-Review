import cv2
import numpy as np

#Reading two different images from the Images folder
img1 = cv2.imread('.\Images\image3.jpg')
img2 = cv2.imread('.\Images\image4.jpg')

#Adding these images into a single image
img = cv2.add(img1, img2) #One constraint of adding images is that the images should have equal dimensions as well as datatype

#Displaying the added images and individual images on the screen
cv2.imshow('First Image', img1)
cv2.waitKey(0)

cv2.imshow('Second Image', img2)
cv2.waitKey(0)

cv2.imshow('Added Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

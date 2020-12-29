import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\image1.jpg', cv2.IMREAD_COLOR) #Making sure that only BGR channels are present without transparency

cv2.imshow('Real Image', img)
cv2.waitKey(0)

#Get the different colour channels of the image
b,g,r = cv2.split(img) #Splits image into the three different channels of lue, green and red (Less efficient than Array Index Slicing)

#Using the blue channel only
bimg = img.copy() #Creates a copy of the image matrix
bimg[:, :, 1] = 0 #Setting all green values of image to 0
bimg[:, :, 2] = 0 #Setting all red values of image to 0
cv2.imshow('Blue Channel Image', bimg)
cv2.waitKey(0)


#Using the green channel only
gimg = img.copy() #Creates a copy of the image matrix
gimg[:, :, 0] = 0 #Setting all blue values of image to 0
gimg[:, :, 2] = 0 #Setting all red values of image to 0
cv2.imshow('Green Channel Image', gimg)
cv2.waitKey(0)


#Using the red channel only
rimg = img.copy() #Creates a copy of the image matrix
rimg[:, :, 0] = 0 #Setting all blue values of image to 0
rimg[:, :, 1] = 0 #Setting all green values of image to 0
cv2.imshow('Red Channel Image', rimg)
cv2.waitKey(0)


#Using the blue and green channels 
bgimg = img.copy() #Creates a copy of the image matrix
bgimg[:, :, 2] = 0 #Setting all red values of image to 0
cv2.imshow('Cyan Channel Image', bgimg)
cv2.waitKey(0)


#Using the green and red channels
grimg = img.copy() #Creates a copy of the image matrix
grimg[:, :, 0] = 0 #Setting all blue values of image to 0
cv2.imshow('Yellow Channel Image', grimg)
cv2.waitKey(0)


#Using the red and blue channels
rbimg = img.copy() #Creates a copy of the image matrix
rbimg[:, :, 1] = 0 #Setting all green values of image to 0
cv2.imshow('Magenta Channel Image', rbimg)
cv2.waitKey(0)

cv2.destroyAllWindows()


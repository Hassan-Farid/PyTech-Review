import cv2 
import numpy as np

#Reading image from Images folder
img = cv2.imread(".\Images\image2.jpg")

#Accessing the dimensions of the image matrix
print("Dimensions of Colored Image are: {}".format(img.shape)) #Here the third argument specifies the different color channels present in the image 

#For grayscale images, the shape returns only two tuple values
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Dimensions of GrayScale Image are: {}".format(gray.shape)) #Here there are only two arguments as there is no color channels present in the image

#Accessing the total number of pixels in the image
print("Size of the image is: {}".format(img.size))

#We can get the total number of pixels using .shape method as well
r,c,channels = img.shape
print("Size of the image is: {}".format(r*c*channels)) #For grayscale we use only r and c

#Accessing the data type of the image matrix
print("Data type of image pixels is: {}".format(img.dtype))
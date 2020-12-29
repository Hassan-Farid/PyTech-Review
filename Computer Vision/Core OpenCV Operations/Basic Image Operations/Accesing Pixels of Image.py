import cv2
import numpy as np
import sys

#Reading image from the Images folder
img = cv2.imread('.\Images\image2.jpg')

#Accessing pixel from an image using (row, column) coordinates
px = img[100, 100]
print(px) #Gives us the value of pixel present in the (100,100) coordinate

#Accessing only a particular color of pixels from the image
bpx = img[100, 100, 0] #Gives blue pixel only
gpx = img[100, 100, 1] #Gives green pixel only
rpx = img[100, 100, 2] #Gives red pixel only

print("Blue Pixel: {} \n Green Pixel: {} \n Red Pixel: {}".format(bpx, gpx, rpx))

#Manipulating pixel value for image
img[100, 100] = [255, 0, 255] #This turns previous color of pixel to magenta
print(img[100, 100])

#Another more efficient way of manipulating and accessing pixels is using numpy's builtin methods
px = img.item(100,100,0) #Gives blue pixel
print(px)

img.itemset((100,100,0), 90) #Assigns the value 90 to the blue pixel
img.itemset((100,100,1), 135) #Assigns the value 135 to the green pixel
img.itemset((100,100,2), 126) #Assigns the value 126 to the red pixel
print(img[100,100])

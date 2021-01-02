import cv2
import numpy as np
import sys

#Read the images from the Images folder
img1 = cv2.imread(".\Images\messi.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(".\Images\soccerball.jpg", cv2.IMREAD_GRAYSCALE)

#Extracting rows, columns and channels of the second image (Soccerball)
rows, cols = img2.shape
print(rows, cols)

#Using these rows we can extract the amount of ROI we need from other image
x,y = 250, 150 #Coordinates where we need to paste the image
ROI = img1[y:rows+y, x:cols+x]
#cv2.imshow('ROI', ROI)
#cv2.waitKey(0)

#Creating mask and mask inverse from the second image (Mask would contain image to be moved while mask inverse will contain everything not to move)
thresh_val = 5
thresh_max = 255
thresh_type = cv2.THRESH_BINARY

ret, mask = cv2.threshold(img2, thresh_val, thresh_max, thresh_type)
mask_inv = cv2.bitwise_not(mask) #Includes all pixels not included in mask 

#Removing the part where to put soccerball in img1
img1_bg = cv2.bitwise_and(ROI, ROI, mask = mask_inv) 

#Displaying the bitmask for ROI
cv2.imshow('Image1 BG Mask', img1_bg)

#Extracting region to put in image1 from image2
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

#Displaying the bitmask for ROI
cv2.imshow('Image2 FG Mask', img2_fg)
cv2.waitKey(0)

#Displaying both images individually
cv2.imshow('Messi', img1)
cv2.imshow('Football', img2)
cv2.waitKey(0)

#Adding the background and foreground and modifying image1 by putting the image in it
dst =  cv2.add(img1_bg, img2_fg)
img1[y:rows+y, x:cols+x] = dst

#Displaying the modified image
cv2.imshow('Modified Messi', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
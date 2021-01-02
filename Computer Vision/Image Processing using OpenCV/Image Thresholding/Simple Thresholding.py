import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread(".\Images\cricketballs.jpg")

#Converting image into grayscale to apply thresholding easily
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Threshold value and Max value to use when applying different thresholdings
thresh = 127
maxval = 255

#Applying binary threshold (Assigns the maxval to the pixel if greater than thresh value otherwise assigns it the value 0)
#Converts all pixels greater than 127 to 255 (i.e. white) and others to 0 (i.e. black)
ret, binary = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY) 

#Applying inverse binary threshold (Assigns the mexval to the pixel if less than thresh value otherwise assigns it the value 0)
#Converts all pixels less than 127 to 255 (i.e. white) and others to 0 (i.e. black)
ret, binary_inv = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV)

#Applying trucate threshold (Assigns the threshold value to the pixel if greater than thresh value otherwise assigns it the value 0)
#Converts all pixels greater than 127 to 127 (i.e. gray) and others to 0 (i.e. black)
ret, trunc = cv2.threshold(img, thresh, maxval, cv2.THRESH_TRUNC)

#Applying to_zero threshold (Assigns every pixel with value less than thresh value to 0)
#Converts all pixels less than 127 to 0 (i.e. black)
ret, zero = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO)

#Applying inverse to_zero threshold (Assigns every pixel with value greater than thresh value to 0)
#Converts all pixels greater than 127 to 0 (i.e. black)
ret, zero_inv = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO_INV)

#Displaying actual image with all the threshold images
cv2.imshow('Original', img)
cv2.imshow('Binary', binary)
cv2.imshow('Binary Inverse', binary_inv)
cv2.imshow('Truncate', trunc)
cv2.imshow('To Zero', zero)
cv2.imshow('To Zero Inverse', zero_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
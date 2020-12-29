import cv2
import numpy as np

#Reading the image from Images
img = cv2.imread(".\Images\image1.jpg")

#Configuring the settings for the border
pad_top = pad_bottom = pad_left = pad_right = 20 #All paddings are set to 20px

#Applying different kinds of borders on the image

#Constant Border i.e. replaces the provided padding with a solid color filled border
value = [0, 255, 255] #Colouring the border Yellow (only applicable for CONSTANT BORDER)
const = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=value)
cv2.imshow('Constant Border Image', const)
cv2.waitKey(0)

#Replicate Border i.e. replaces the provided padding with a replicated image border
replicate = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_REPLICATE)
cv2.imshow('Replicate Border Image', replicate)
cv2.waitKey(0)

#Reflect Border i.e. replaces the provided padding with a reflected image border
reflect = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_REFLECT)
cv2.imshow('Reflect Border Image', reflect)
cv2.waitKey(0)

#Reflect 101 Border i.e. replaces the provided padding with a reflected image border with slight adjustment
reflect101 = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_REFLECT_101)
cv2.imshow('Reflect 101 Border Image', reflect101)
cv2.waitKey(0)

#Wrap Border i.e. replaces the provided padding with a wrapped image border
wrap = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_WRAP)
cv2.imshow('Wrap Border Image', wrap)
cv2.waitKey(0)

cv2.destroyAllWindows()


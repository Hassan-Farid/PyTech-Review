import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread(".\Images\cricketballs.jpg")

#Converting image into grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Configurating settings for the otsu binarization
thresh = 0
maxval = 255

#Applying Otsu Binarization on the grayscale image
ret, res = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#Displaying the images
cv2.imshow('GRAYSCALE IMAGE', img)
cv2.imshow('OTSU BINARIZED IMAGE', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
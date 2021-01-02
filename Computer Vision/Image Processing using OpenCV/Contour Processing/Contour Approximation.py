import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/incomplete_rect.jpg')

#Converting image into grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Computing contour for the provided image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing the maximum possible distance from the actual contour
epsilon = 0.1 * cv2.arcLength(cnts[0], True)

#Applying Douglas-Pecker algorithm with the help of maximum possible distance
approx = cv2.approxPolyDP(cnts[0], epsilon, closed=True)

#Creating image to display contour and its approximated version on
white = np.ones((512,512,3), np.uint8) * 255
white2 = white.copy()

for c in cnts:
    cv2.drawContours(white, [c], -1, (0,255,0), -1)
    epsilon = 0.03 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, False)
    cv2.drawContours(white2, [approx], -1, (0,255,0), -1) 

#Displaying images
cv2.imshow('Original Image', img)
cv2.imshow('Normal Contour Image', white)
cv2.imshow('Approximated Contour Image', white2)

cv2.waitKey(0)
cv2.destroyAllWindows()
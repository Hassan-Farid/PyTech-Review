import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/cross.jpg')

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating contours of the image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing the area of the contour

#Using the moment of images as shown previously
moments = cv2.moments(cnts[0])

print('Area of the Contour is: {}'.format(moments['m00']))

#Using the builtin opencv method to find the are of contour
area = cv2.contourArea(cnts[0])
print('Area of the Contour is: {}'.format(area))


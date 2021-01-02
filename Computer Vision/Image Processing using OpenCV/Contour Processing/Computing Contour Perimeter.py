import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread("./Images/cross.jpg")

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Finding contours from the image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing the perimeter for the found contours
isclosed = True #Specifies whether the provided image is closed or not

perimeter = cv2.arcLength(cnts[0], isclosed)

print("The perimeter of the contour in the image is: {}".format(perimeter))
import cv2
import numpy as np

#Reading images from the Images folder
star = cv2.imread("./Images/star.jpg")
cross = cv2.imread("./Images/cross.jpg")

#Converting images into grayscale
star = cv2.cvtColor(star, cv2.COLOR_BGR2GRAY)
cross = cv2.cvtColor(cross, cv2.COLOR_BGR2GRAY)

#Finding contours for the image
star_cnts, _ = cv2.findContours(star, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cross_cnts, _ = cv2.findContours(cross, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Taking into consideration the first contour only
c1 = star_cnts[0]
c2 = cross_cnts[0]

#Finding match rate of both contours
matchRate = cv2.matchShapes(c1, c2, 1, 0.0) #Uses Hu Moments to match the provided contours

#Displaying the result on the screen
print("Match rate of the provided Star and Cross Shapes is: {}".format(matchRate))
import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread("./Images/cross.jpg")

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Finding contours for the provided image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Consider the first contour from the list of contours
c = cnts[0]

#Create a function for finding Point Location w.r.t Contour
def pointCheck(contour, point):
    pointPos = cv2.pointPolygonTest(contour, point, measureDist=False) #Gets the result whether the point is above below or on the contour
    if pointPos == 1:
        print("{} is inside the Contour".format(point))
    elif pointPos == -1:
        print("{} is outside the Contour".format(point))
    else:
        print("{} is lieing on the Contour".format(point))
    
#Finding the location of points for various points
pointCheck(c, (38, 76))
pointCheck(c, (138, 76))
pointCheck(c, (129, 76))

#Create a function for function for finding Point Distance from the Contour
def getPointDistance(contour, point):
    pointDist = cv2.pointPolygonTest(contour, point, measureDist=True) #Gets the distance of a point from the contour
    print("Distance of {} from the Contour is {}".format(point, round(pointDist, 3)))
    
#Finding the distance of points for various points from the Contour
getPointDistance(c, (38,76))
getPointDistance(c, (138,76))
getPointDistance(c, (129,76))
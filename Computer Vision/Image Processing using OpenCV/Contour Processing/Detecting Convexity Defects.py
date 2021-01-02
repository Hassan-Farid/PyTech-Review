import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/hands.jpg')
new_img = img.copy()

#Converting into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating a threshold for the image
ret, thresh = cv2.threshold(img, 235, 255, cv2.THRESH_BINARY_INV)

#Finding contours in the thresholded image
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing convex hull and defect in convexity for the first contour
c = cnts[0]

convexHull = cv2.convexHull(c, returnPoints=False) #Returns the corresponding contour points for hull points
defects = cv2.convexityDefects(c, convexHull) #Computes the defects if any in the convexity of the contour

#Creating lines and circles to indicate convexity defects
for i in range(defects.shape[0]):
    start, end, farthest, fdist = defects[i,0] #start point, end point, farthest point, farthest point depth
    start = tuple(c[start][0]) 
    end = tuple(c[end][0])
    farthest = tuple(c[farthest][0])
    cv2.line(new_img, start, end, (0,255,0), 2) #Creates a green line connecting start and end points (Eventually creates the convexhull itself)
    cv2.circle(new_img, farthest, 5, (0,0,255), -1) #Creates filled red circles on points which are fartest from the hull for a contour

#Displaying images on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Defects Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
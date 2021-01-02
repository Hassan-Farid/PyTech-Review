import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread("./Images/cross.jpg")

#Converting into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Finding contours from the image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Viewing the properties of the first contour (Viewing the properties of first contour)
c = cnts[0]

#Aspect Ratio of the Contour
x, y, w, h = cv2.boundingRect(c) #Gives the width and height of the contour which can be used to compute aspect ratio
print("Aspect Ratio of the Contour: {}".format(round(w/h, 2)))

#Extent of the Contour
area = cv2.contourArea(c) #Gives the area occupied by the contour
rect_area = w*h #Gives the area occupied by the bounded rectangle
print("Extent of the Contour: {}".format(round(area/rect_area, 2)))

#Solidity of the Contour
hull = cv2.convexHull(c) #Gives the convex hull of the contour
hull_area = cv2.contourArea(hull) #Gives the area occupied by the convex hull of the contour
print("Solidity of the Contour: {}".format(round(area/hull_area, 2)))

#Equivalent Diameter of the Contour
print('Equivalent Diameter of the Contour: {}'.format(round(np.sqrt(4 * area/np.pi), 2)))

#Orientation of the Contour
center, axes, angle = cv2.fitEllipse(c) #Computes the center, axes and orientation angle to fit an ellipse
#Using the orientation for the fit, we can assume that the contour itself is based on such orientation
print("Orientation of the Contour: {}".format(angle))

#Pixel Points of a Contour
mask = np.zeros(img.shape, np.uint8) #Creating an empty black background image
cv2.drawContours(mask, c, -1, 255, -1) #Draw the first contour on the created mask image
pixelPoints = cv2.findNonZero(mask) #Find all points on the image which carry non-zero value
cv2.imshow('Mask Image', mask) #Displaying all the pixel points on the screen
cv2.waitKey(0)

#Maximum and Minimum Values of the Contour and their respective Location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask=mask) #Computes the required values for the Contour
print("Maximum value of Contour is: {} and its location is: {}".format(max_val, max_loc))
print("Minimum value of Contour is: {} and its location is: {}".format(min_val, min_loc))

#Mean Colour of the Contour
mean_val = cv2.mean(img, mask=mask) #Computes the mean color/intensity of the Contour
print("Mean intensity of the Contour is: {}".format(mean_val))

#Extreme Points of the Contour
leftmost = tuple(c[c[:,:,0].argmin()][0]) #Computes minimum x-value in the image w.r.t contour
rightmost = tuple(c[c[:,:,0].argmax()][0]) #Computes maximum x-value in the image w.r.t contour
topmost = tuple(c[c[:,:,1].argmin()][0]) #Computes minimum y-value in the image w.r.t contour
bottommost = tuple(c[c[:,:,1].argmax()][0]) #Computes maximum y-value in the image w.r.t contour
print("Extreme Values are: Left: {} , Right: {}, Top: {}, Bottom: {}".format(leftmost, rightmost, topmost, bottommost))

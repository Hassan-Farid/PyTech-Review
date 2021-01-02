import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/electric.jpg')
new_img = img.copy()

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Computing thresholded image
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

#Finding contour points from the image
cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing the parameters for fitting the line and drawing it on the image
rows, cols = new_img.shape[:2] #Storing the first two values as the third one is the "channels" value

#Configuring settings for the fitted line
distType = cv2.DIST_L2 #Performs the most basic form of LSM
param = 0 #Chooses an optimal value of numerical parameter for the distance type
reps = 0.01 #Setting accuracy for the radius of the fit
aeps = 0.01 #Setting accuracy for the angle of the fit

for c in cnts:
    #Computing normalized vector coordinates (vx,vy) collinear to the line and coordinates (x,y) lieing on the line
    [vx, vy, x, y] = cv2.fitLine(c, distType, param, reps, aeps)     
    
    #Computing left and right points to create a line
    left = int((-x * vy/vx) + y)
    right = int(((cols - x) * vy/vx) + y)  
    
    #Creating a line using the created left and right points
    new_img = cv2.line(new_img, (cols - 1, right), (0, left), (0, 255, 0), 2)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Fitted Line Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()  
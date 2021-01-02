import cv2
import numpy as np
import sys

#Reading image from the Images folder (In grayscale format)
img = cv2.imread('./Images/rect.jpg', 0)

if img is None:
    sys.exit('Could not find the image in specified folder')

#Extracting contours from this image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

if cnts is None:
    sys.exit('Could not find any contours in the image')

#Drawing these contours on another image with white background
new_img = np.ones((512,512,3), np.uint8) * 255
for c in cnts:
    cv2.drawContours(new_img, [c.astype(int)], contourIdx=-1, color=(0,255,0), thickness=-1) #Drawing filled contours

#Displaying the image on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Contour Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
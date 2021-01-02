import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('./Images/cross.jpg')

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Computing contours from the image
cnts, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Computing image moments for the contours 
moments = dict()
for c in cnts:
    moments.update(cv2.moments(c)) 
    
#Displaying contents obtained from the moments 
for m,v in moments.items():
    print('{}'.format((m,v)))

#We can use these moments to compute different properties regarding the contour

#Computing the area of the contour
print('Area of the Contour is: {}'.format(moments['m00']))

print('Centroid of the Contour is: {}'.format((moments['m10']/moments['m00'], moments['m01']/moments['m00'])))

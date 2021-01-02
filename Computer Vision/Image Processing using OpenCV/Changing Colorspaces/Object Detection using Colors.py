import cv2
import numpy as np
import sys

#Reading image from the Images folder
img = cv2.imread(".\Images\cricketballs.jpg")

if img is None:
    sys.exit("Could not find the image in the specified folder")

#Converting the image into HSV format
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Creating HSV bounds (Range of colours which is to be detected)
lower_bound = np.array([0, 215, 215]) #Equivalent to light yellow in BGR
upper_bound = np.array([30, 255, 255]) #Equivalent to pure yellow in BGR

#Detecting objects within the provided HSV color channel range (Creating a mask for such objects)
mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

#Applying mask on the actual image to get the object
obj = cv2.bitwise_and(img, img, mask=mask)

#Displaying the image
cv2.imshow("Actual Image", img)
cv2.imshow("Object Image", obj)

cv2.waitKey(0)
cv2.destroyAllWindows()
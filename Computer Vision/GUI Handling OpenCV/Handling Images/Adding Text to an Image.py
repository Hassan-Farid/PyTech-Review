import cv2
import sys
import numpy as np
import os

#Loading image from the Images folder
img = cv2.imread(".\Images\image1.jpg") #Reads image in BGR mode

if img is None:
    sys.exit("Image not found at specified path")

#Asking for the text to write on the image as user input
text = input("Enter the text that you want to display on the image: ")

#Configuring settings for the text to be displayed on the image
font = cv2.FONT_HERSHEY_SIMPLEX #Font family for the text
bottom_left_pts = (170,170) #Coordinates where to start text
font_size = 2 #in pixel
color = (0,0,0) #white BGR code
line_width = 4 #in pixel
line_type = cv2.LINE_AA #Specifying type of line (anti-aliasing)

#Displaying text on the image
img = cv2.putText(img, text, bottom_left_pts, font, font_size, color, line_width, line_type)

#Displaying image on the screen
cv2.imshow("Text Image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
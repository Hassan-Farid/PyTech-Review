import cv2
import numpy as np

#Reading images from the Image folder
img = cv2.imread(".\Images\image2.jpg")

#Getting the Region of Image where the Bird is located using a rectangle shape
cv2.namedWindow('Before ROI Window')

#Displaying the image and the rectangle with it
rect_img = cv2.rectangle(img, (155,115), (380,325), (0,255,0), 2, cv2.LINE_AA) #Creating a green rectangle with anti-alaising lines
cv2.imshow('Before ROI Window', img)
cv2.waitKey(0)

#Now since we are certain that the bird's image is there, we can use this image and replace it with equivalent number of pixels 
#This operation is shown as under. The result will be 2 birds in the new image
width = 380 - 155  #Computing width of rectangle
height = 325 - 115 #Computing height of rectangle

#Now using the ROI to copy paste the image of the bird
x, y = 75, 350 #Starting coordinates where to paste the image
bird = img[115:325, 155:380] #Getting the coordinates of bird

#Displaying image after apply copy paste using ROI 
img[y:y+height, x:x+width] = bird
cv2.imshow('After ROI Window', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
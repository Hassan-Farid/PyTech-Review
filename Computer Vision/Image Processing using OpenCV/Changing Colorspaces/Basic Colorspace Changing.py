import cv2
import numpy as np

#Reading the different kinds of FLAGs available for colorspace conversion
flags = list(i for i in dir(cv2) if i.startswith('COLOR_'))
for x in flags:
    print(x)
    
#Reading image from the Images folder
img = cv2.imread(".\Images\cricketballs.jpg")

#Converting the image from BGR to usually used formats
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Grayscale Format
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #HSV Format
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #RGB Format
rgba_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA) #RGBA Format

#Displaying image on the screen
cv2.imshow("BGR Image", img)
cv2.imshow("GRAYSCALE Image", gray)
cv2.imshow("HSV Image", hsv_img)
cv2.imshow("RGB Image", rgb_img)
cv2.imshow("RGBA Image", rgba_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
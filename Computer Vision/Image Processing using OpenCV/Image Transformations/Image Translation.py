import cv2
import numpy as np

#Creating an image
img = np.zeros((512,512,3), np.uint8)

#Creating a filled circle on the image
img = cv2.circle(img, (255,255), 50, (255,0,0), -1) #Creates a filled blue circle at (255,255) with radius 50px

#Configuring settings for the translation transformation
tx = 100 #Translate by 100px along x axis
ty = 50 #Translate by 50px along y axis

#Creating the transformation matrix
translate = np.float32([[0,1,tx], [1,0,ty]]) #Opencv doesn't provide a general method to create a translation transform

#Applying the translation matrix to the image
res = cv2.warpAffine(img, translate, dsize=img.shape[1::-1], flags=cv2.INTER_LINEAR)

#Displaying the image on the screen
cv2.imshow('Original Image', img)
cv2.imshow('Translated Image', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
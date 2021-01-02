import cv2
import numpy as np

#Reading the image from Images folder
img = cv2.imread('.\Images\holes_A.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for the Black Hat Transform
ksize = 5
kernel = np.ones((ksize, ksize), np.uint8)
op = cv2.MORPH_BLACKHAT

#Applying the Black Hat Transform on the image
black_img = cv2.morphologyEx(img, op, kernel)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Black Hat Transform Image', black_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
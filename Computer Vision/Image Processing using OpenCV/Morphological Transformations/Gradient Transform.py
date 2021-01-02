import cv2
import numpy as np

#Reading image from the Images folder
img = cv2.imread('.\Images\A.jpg', cv2.IMREAD_GRAYSCALE)

#Configuring settings for applying Gradient Transform
ksize = 5
kernel = np.array((ksize, ksize), np.uint8)
op = cv2.MORPH_GRADIENT

#Applying the gradient transform on the image
grad_img = cv2.morphologyEx(img, op, kernel)

#Displaying the images
cv2.imshow('Original Image', img)
cv2.imshow('Graident Transform Image', grad_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2 
import numpy as np
import sys

#Reading image from the Images folder
img = cv2.imread('.\Images\grid.jpg')

if img is None:
    sys.exit("Image not found in the specified folder")

#Configuring settings for the affine transformation
before_pts = np.float32([[82,82], [82,162], [162,82]]) #Points whose location is to be changed w.r.t. affine transformation
after_pts = np.float32([[72,102], [82,162], [172, 62]]) #New location of the above points w.r.t. affine transformation
dsize = img.shape[1::-1] #Gets the size of the original image

#Creating the affine transformation matrix
affine = cv2.getAffineTransform(before_pts, after_pts)

#Applying the affine transformation matrix on the image
res = cv2.warpAffine(img, affine, dsize, flags=cv2.INTER_LINEAR)

#Displaying the images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation Image", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
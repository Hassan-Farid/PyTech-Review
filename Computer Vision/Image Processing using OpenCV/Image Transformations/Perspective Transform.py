import cv2
import numpy as np

#Reading image from the images folder
img = cv2.imread('.\Images\grid.jpg')

#Configuring settings for the perspective transformation
before_pts = np.float32([[42,54], [152, 40], [22, 169], [171,172]]) #Before change of perspective
after_pts = np.float32([[0,0], [122, 0], [0, 122], [122, 122]]) #After change of perspective
dsize = (122,122) #(Rows, Columns) of the image after perspective change

#Creating perspective transformation matrix
pers = cv2.getPerspectiveTransform(before_pts, after_pts) 

#Applying the perspective transform on the provided image
res = cv2.warpPerspective(img, pers, dsize, flags=cv2.INTER_LINEAR)

#Resizing the final image to view result clearly
res = cv2.resize(res, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

#Displaying the images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transform Image", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

#Creating a black image
img = np.zeros((512, 512, 3), np.uint8)

#Creating polynomial using array of points
pt_array = np.array([[125,125], [250,0], [375,125], [313,250], [163,250]], np.int32)

#Reshaping array into proper shape 
pt_array = pt_array.reshape((-1,1,2))

#Displaying closed polygon on the image using the above mentioned points 
is_closed = True
color = (255,255,255) #white BGR code
line_width = 4 #in pixels
line_type = cv2.LINE_AA

img = cv2.polylines(img, [pt_array], is_closed, color, line_width, line_type)

#Displaying image on the screen
cv2.imshow('Polygon', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
import numpy as np

#Crreating an image
img = np.zeros((512, 512, 3), np.uint8)

#Drawing a triangle on the image
vertices = np.array([[280, 200], [50, 450], [400, 450]], np.int32)
pts = vertices.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0,255,0))

#Configuring the settings for the rotation transformation
vertice_sum = map(sum, zip(*vertices)) #Gives the sum of all x coords and y coords of vertices of the triangle
center = tuple(round(x/3, 2) for x in vertice_sum) #Gives the centroid of the traingle (It is the center from which we have to rotate the image)
scale = 1 #Since we don't want to scale the image just rotate it

#Creating rotation matrices at different angles
rotate45 = cv2.getRotationMatrix2D(center, angle=45, scale=scale)
rotate90 = cv2.getRotationMatrix2D(center, angle=90, scale=scale)
rotate135 = cv2.getRotationMatrix2D(center, angle=135, scale=scale)
rotate180 = cv2.getRotationMatrix2D(center, angle=180, scale=scale)

#Creating rotated images using the created rotated matrices
#This warpAffine method allows to map a certain transformation matrix on an image and return the resultant image
img45 = cv2.warpAffine(img, rotate45, dsize=img.shape[1::-1], flags=cv2.INTER_LINEAR) #dsize = (rows x columns) of image to be applied to
img90 = cv2.warpAffine(img, rotate90, dsize=img.shape[1::-1], flags=cv2.INTER_LINEAR)
img135 = cv2.warpAffine(img, rotate135, dsize=img.shape[1::-1], flags=cv2.INTER_LINEAR)
img180 = cv2.warpAffine(img, rotate180, dsize=img.shape[1::-1], flags=cv2.INTER_LINEAR)

#Displaying image on the screen
cv2.imshow('0deg Triangle', img)
cv2.imshow('45deg Triangle', img45)
cv2.imshow('90deg Triangle', img90)
cv2.imshow('135deg Triangle', img135)
cv2.imshow('180deg Triangle', img180)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import sys

#Reading image from the Images folderl
img = cv2.imread(".\Images\image1.jpg")

#Creating a named window to load image in
cv2.namedWindow('Auto Image Window', cv2.WINDOW_AUTOSIZE) #Creates an autosized window to load image in (Default value)

#Creating a named window to load image in
cv2.namedWindow('Normal Image Window', cv2.WINDOW_NORMAL) #Creates a normal window (resizable)

#Checking if the image is in the specified path
if img is None:
    sys.exit("Image not found in the specified path")

#Displaying image in both windows
cv2.imshow('Auto Image Window', img)
cv2.waitKey(0)

cv2.imshow('Normal Image Window', img)
cv2.waitKey(0)

#Destroying all opened GUI windows
cv2.destroyAllWindows()

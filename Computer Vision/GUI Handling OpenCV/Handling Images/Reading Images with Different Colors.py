import cv2
import sys

#Reading image from the Images folder in Grayscale Format
grey_img = cv2.imread("./Images/image1.jpg", cv2.IMREAD_GRAYSCALE) #Alternatively use 0

#Reading image from Image folder neglecting transparency value (Converts RGBA/BGRA to RGB/BGR)
color_img = cv2.imread("./Images/image1.jpg", cv2.IMREAD_COLOR) #Alternatively use 1

#Reading image from Image folder without changing any characteristics of the image (loads alpha channel as well)
img = cv2.imread("./Images/image1.jpg", cv2.IMREAD_UNCHANGED) #Alternatively use -1

#Checking if the image loads successfully
if img is None:
    sys.exit("Image not found at specified Path")

#Displaying the three different types of images
#Displaying Grayscale Image
cv2.imshow("Grayscale Image", grey_img)
cv2.waitKey(0)

#Dispalying RGB Image
cv2.imshow("RGB Image", color_img)
cv2.waitKey(0)

#Displaying Unchanged Image
cv2.imshow("Unchanged Image", img)
cv2.waitKey(0)

#Destroy all opened windows
cv2.destroyAllWindows()

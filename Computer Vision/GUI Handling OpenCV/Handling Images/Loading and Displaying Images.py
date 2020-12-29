import cv2
import sys

#Reading the image from the Images folder
img = cv2.imread(".\Images\image1.jpg")

#Checking the type of the img oject
print(type(img)) #object will be of class: numpy.ndarray since pixels are in a form of n-dim array to form an image

#Checking if the image was loaded correctly
if img is None:
    sys.exit("Image could not be loaded!")
    
#If image was loaded correctly, then we can display it using the following:
cv2.imshow("Image1", img)

#Exiting the image prompt/screen until any key is pressed
k = cv2.waitKey(0) #0 milliseconds => Infinite time

#Saving the image if needed on pressing the key 's
if k == ord('s'):
    cv2.imwrite("New_Image1.png", img)
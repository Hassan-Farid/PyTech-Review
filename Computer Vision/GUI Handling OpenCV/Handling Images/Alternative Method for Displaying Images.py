import cv2
import sys
import matplotlib.pyplot as plt

#Displaying GRAYSCALE Image using Matplotlib

#Reading image from the Images folder
img = cv2.imread('.\Images\image1.jpg', cv2.IMREAD_GRAYSCALE)

#Checking if the image exists or not
if img is None:
    sys.exit('Image not found in the specified folder')

#Displaying the image using Matplotlib
plt.imshow(img, cmap = 'gray', interpolation='bicubic') #Configuring the setting for the image that is to be displayed
plt.xticks([]) #removes x ticks from the displayed image
plt.yticks([]) #removes y ticks from the displayed image
plt.show() #Displays the image on the screen

#Displaying COLOURED Image in Matplotlib

#Reading the image from the Images folder
img = cv2.imread('.\Images\image1.jpg', cv2.IMREAD_COLOR)

#Displaying the image using Matplotlib
#Before we change the image it should be noted that OpenCV reads images as BGR whereas Matplotlib processes images as RGB
cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #This converts the image read by opencv to RGB convention

plt.imshow(img) #Configuring setting for the image that is to be displayed
plt.xticks([]) #removes x ticks from the displayed image 
plt.yticks([]) #removes y ticks from the displayed image
plt.show() #Displays the image on the screen

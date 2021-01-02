import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading image from the Images folder
img = cv2.imread('./Images/cricketballs.jpg')

#Converting image into Grayscale image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating a mask to extract a particular subset of image
mask = np.zeros(img.shape[:2], np.uint8) #Creating an empty black bg image to put subset of image in
mask[110:185, 60:140] = 255 #Assigning area of subset of image to white pixels
masked_img = cv2.bitwise_and(img, img, mask=mask) #Successfully shifts the subset of image to the masked_img

#Displaying images
cv2.imshow('Original Image', img)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', masked_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Now plotting the histogram with mask and without mask
hist_full = cv2.calcHist([img], [0], None, [255], [0,256])
hist_mask = cv2.calcHist([img], [0], mask, [255], [0,256])

plt.plot(hist_full) #Plots full image histogram
plt.plot(hist_mask) #Plots masked image histogram
plt.xlim([0,256]) #Creates a limit of x-ticks from 0 to 256

plt.show() #Display histogram on the screen

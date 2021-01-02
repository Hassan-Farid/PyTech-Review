import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading image from the Images folder
img = cv2.imread('./Images/image4.jpg')

#Converting image into grayscale format
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Configuring settings for calculating the image histogram
channel = [0] #Since image is grayscale thus there is only one channel
mask = None #Since we need to compute histogram for full image. Otherwise we can use mask to remove unnecessary pixels from the image
histSize = [256] #Bin count for the histogram (There will be 256 bins each representing 1 value from 0-255 color value)
ranges = [0, 256] #Histogram ranging from 0 to 256

#Computing histogram from the image histogram
hist = cv2.calcHist(img, channel, mask, histSize, ranges)

#Displaying the image histogram
plt.plot(hist) #Using plot method to display an histogram
plt.show() #Using show method to display the image
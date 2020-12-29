import cv2
import numpy as np

#Create a method which does not perform any type of functionality (we just want to change the color of image based on trackbars)
def do_nothing(x): #Passing a parameter as createTracker method takes a TrackerCallback Method with 1 parameter
    pass

#Creating a black image
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Trackbar Colour Changer')

#Now creating Trackbar Objects
cv2.createTrackbar('Red Slider', 'Trackbar Colour Changer', 0, 255, do_nothing)
cv2.createTrackbar('Blue Slider', 'Trackbar Colour Changer', 0, 255, do_nothing)
cv2.createTrackbar('Green Slider', 'Trackbar Colour Changer', 0, 255, do_nothing)

#Creating a Trackbar that allows to get the values from the previous three trackbars and change the image colour accordingly
cv2.createTrackbar('Colour Switch', 'Trackbar Colour Changer', 0, 1, do_nothing)

#Displaying the window till user exits the GUI
while True:
    cv2.imshow('Trackbar Colour Changer', img)
    k = cv2.waitKey(1)
    if k == 27: #Terminate if key pressed is 'ESC'
        break
    
    #Get the positions of the trackers
    r = cv2.getTrackbarPos('Red Slider', 'Trackbar Colour Changer')
    b = cv2.getTrackbarPos('Blue Slider', 'Trackbar Colour Changer')
    g = cv2.getTrackbarPos('Green Slider', 'Trackbar Colour Changer')
    
    #Get the value of the switch for the last tracker and apply changes to the image accordingly
    s = cv2.getTrackbarPos('Colour Switch', 'Trackbar Colour Changer')
    
    #If switch value is 1, apply changes
    if s == 1:
        img[:] = [b, g, r]
    else:
        img[:] = 0
    
#Terminate all opened windows
cv2.destroyAllWindows()


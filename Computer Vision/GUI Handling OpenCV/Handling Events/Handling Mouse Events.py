import cv2
import numpy as np

#Listing all the possible events provided in opencv
eventList = list(i for i in dir(cv2) if 'EVENT' in i)

for x in eventList:
    print(x)
    
#Lets create a circle on an image using the event "MBUTTONDBLCLK" 

#Creating the Event Callback Function (Function called whenever the Mouse Button is clicked Twice)
def draw_circle(event, x, y, flags, param):
    props = (10, (255,255,255), 3) #Tuple comprising of the properties of the circle to be drawn 
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), *props)
        
#Creating a image window to display the circle
img = np.zeros((512,512,3), np.uint8) #Creates a black image of 512x512 pixels
cv2.namedWindow('Circle Painter')
cv2.setMouseCallback('Circle Painter', draw_circle)

#Run application until ESC key is pressed
while True:
    cv2.imshow('Circle Painter', img)
    key = cv2.waitKey(0)
    if key == 27: #Represents the ESC key
        break
    
#Terminating all Windows
cv2.destroyAllWindows()

    

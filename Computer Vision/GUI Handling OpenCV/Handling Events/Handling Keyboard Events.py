import cv2
import numpy as np

#Defining global coordinates for the points
ix, iy = -1, -1

#Creating a keyboard callback function
def set_mouse_pointer(event, x, y, flags, param):
    global ix, iy
    ix, iy = x, y #Assign the global coordinates equal to the location of the mouse cursor
    
#Creating a black image on a named Window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Circle Painter')
cv2.setMouseCallback('Circle Painter', set_mouse_pointer)

#Calling the callback method using Keyboard
while True:
    cv2.imshow('Circle Painter', img)
    k = cv2.waitKey(0) & 0xFF
    #Creates a circle when the key 'c' is pressed
    if k == ord('c'):
        radius = 10
        color = (255, 0, 0) #blue BGR code
        line_width = -1 #Fill circle
        
        cv2.circle(img, (ix,iy), radius, color, line_width)
    #Creates a rectangle when the key 'r' is pressed
    elif k == ord('r'):
        width = 100
        height = 100
        color = (0,255,0) #green BGR code
        line_width = -1 #Fill circle
        
        cv2.rectangle(img, (ix, iy), (ix+width, iy+height), color, line_width)
    #Terminates the window when the key 'q' is pressed
    elif k == ord('q'):
        break
    
cv2.destroyAllWindows()
        
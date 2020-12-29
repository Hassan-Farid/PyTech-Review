import cv2
import numpy as np

#Create a black image of size 512x512 pixels (Create a numpy n-dim array filled with 0's)
img = np.zeros((512, 512, 3), np.uint8) 

#Drawing a line on the created image
start_point = (0,0) #Draws a line from top left corner of image (X-axis goes left to right whereas Y-axis goes top to bottom as value of (x, y) increases)
end_point = (250,250)
line_color = (255,255,255) #white BGR code
line_width = 4 #in pixels
img = cv2.line(img, start_point, end_point, line_color, line_width)

#Drawing an anti-aliased line on the created image
start_point = (0,0)
end_point = (160, 370)
line_color = (255,255,255) #white BGR code
line_width = 4 #in pixels
img = cv2.line(img, start_point, end_point, line_color, line_width, cv2.LINE_AA)

#Drawing a rectangle on the created image
top_left_point = (50,50)
bottom_right_point = (250,250)
line_color = (0, 255, 0) #green BGR code
line_width = 4 #in pixels
img = cv2.rectangle(img, top_left_point, bottom_right_point, line_color, line_width)

#Drawing a circle on the created image
center = (300,300)
radius = 70 #in pixels
circle_color = (255, 0, 0) #blue BGR code
line_width = 4 #in pixels
img = cv2.circle(img, center, radius, circle_color, line_width)

#Drawing an ellipse on the created image
center = (230, 370)
axes_length = (70, 30) #(major_axis_length, minor_axis_length)
rot_angle = 0 #Rotation angle of ellipse anti-clockwise
startAngle, endAngle = 0, 180 #Starting and Ending angles of ellipse arc w.r.t. major axis
color = (0, 0, 255) #red BGR code
line_width = 4 #in pixels
img = cv2.ellipse(img, center, axes_length, rot_angle, startAngle, endAngle, color, line_width)

#Displaying the image
cv2.imshow("Image with Shapes", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
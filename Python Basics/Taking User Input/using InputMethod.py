'''
    For user input, we use the input() method which allows the user to type a particular input
'''

#Using the input method to take a message like "Hello World"
message = input() #Allows user to type in some sort of text message
print(message) #Display the message on the screen

#Using the input method to take an integer number
num = int(input())
print("The inputted number is {}".format(num))

#Using the input method to give user a certain prompt which tells the user what type of input the program wants
message = input("Please enter a text message: ")
print("The inputted text message is: {}".format(message))

num = int(input("Please enter an integer: "))
print("The inputted number is: {}".format(num))

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Take the following inputs by providing prompts to user:

Enter the first point's x coordinate: __________ (Input comes in the blank)
Enter the first point's y coordinate: __________ (Input comes in the blank)
Enter the second point's x coordinate: ___________ (Input comes in the blank)
Enter the second point's y coordinate: ___________ (Input comes in the blank)

Once input has been taken, you can use print formatting to display ouput in the format:

First point coordinates: (2, 5)
Second point coordinates: (7, 8)
The slope of the line through these points is given as follows:

    m = (y2 - y1)/(x2 - x1)
    m = (8 - 5)/(7 - 2)
    m = 3/5

which is the required slope of the provided coordinates

'''
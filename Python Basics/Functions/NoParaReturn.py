'''
    Although the use of these function is rare as well, but it come in handy to know this type of function as well.
    The No Parameter Return Value Function doesn't take any argument values but returns a value that can be stored into a variable.
'''

def returnHello(): #Takes no argument values
    return "Hello World!" #Returns the message "Hello World" which can be stored in a variable 

#Calling the Function
message = returnHello() #Stores the return value of the function into the message variable
print("The message returned by the method is: {}".format(message))

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses a no para return function, that returns the value of a variable taken as input within the function.
Execution of the function should give the result like:

Enter a message to display using this function: _______________ (Input in the blank)

Once called, store the returned value of the function in a message variable and then output it on the screen like:

Message: _________________ (Text inputted by user in the blank) 

'''
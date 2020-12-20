'''
    Although the use of these function is rare as well, but it come in handy to know this type of function as well.
    The Parameter No Return Value Function takes an argument value and uses that argument value to display a message on screen.
'''

def print_arg_sum(a, b): #Takes two integers as input
    print("Sum of the numbers {0} and {1} is {2}".format(a, b, a + b))
    
#Calling the function
print("This is the print_arg_sum Method, which displays the sum of the two arguments passed to it \n")
print_arg_sum(2,3) #Displays the message on screen with the sum of the two arguments

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses a para no return function, that displays the average of three arguments passed to it.
Execution of the function should give the result like:

Average of Arguments: 4 (Arguments passed: 3, 4, 5)

'''
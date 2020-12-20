'''
    Most of the time, there is a need for looping through a particular values of a sequence or create a counter for some purpose.
    The for Loop is one of the most common methods that is used to achieve this goal
'''

#Using the for loop with incrementing counter (default)
for i in range(11): #Prints value of i = 0 to i = 10 with 1 increment each step
    print(i)
    
#Using the for loop starting from some specific value and incrementing counter
for i in range(5,11): #Prints value of i = 5 to i = 10 with 1 increment each step
    print(i)
    
#Using the for loop starting from some specific value and decrementing counter
for i in range(10,4,-1): #Prints value of i = 10 to i = 5 with 1 decrement each step
    print(i)
    
#Using the form loop starting from some specific value and incrementing by a desired step size
for i in range(1,11,2): #Prints value of i = 1 to i = 9 with 2 increment each step
    print(i)

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses For Loop to compute the factorial of a number. Take a number from user with the prompt:

Enter an integer: ___________________ (Input comes in blank)

Once the input has been entered, the program should return the factorial of that number. An example would be:

Enter an integer: 7
Factorial of Inputted Number: 5040

'''
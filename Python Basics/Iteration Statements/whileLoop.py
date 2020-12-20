'''
    Most of the time, there is a need for looping through a particular values of a sequence or create a counter for some purpose.
    The while Loop is another common methods that is used to achieve this goal
'''

#Using the while loop with incrementing counter
i = 0 #Initialization is manual in while Loops
while(i <= 10): #Iterates until i reaches the value 10
    print(i)
    i += 1 #Incrementing is also manual in while loop
    
#Using the while loop with some initial value and incrementing counter
i = 5
while (i <= 10):
    print(i)
    i += 1
    
#Using the while loop with decrementing counter
i = 10
while(i >= 0):
    print(i)
    i -= 1
    
#Using the while loop with some initial value and incrementing by desired step
i = 1
while (i <= 10):
    print(i)
    i += 2
    
#Using the while loop with some initial value and decrementing by desired step
i = 10
while (i >= 0):
    print(i)
    i -= 2
    
'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses While Loop to compute the factorial of a number. Take a number from user with the prompt:

Enter an integer: ___________________ (Input comes in blank)

Once the input has been entered, the program should return the factorial of that number. An example would be:

Enter an integer: 7
Factorial of Inputted Number: 5040

'''
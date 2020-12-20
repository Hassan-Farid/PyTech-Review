'''
    Most of the time, there is a need for looping through a particular values of a sequence or create a counter for some purpose.
    The while True Loop is an extension of while loop that uses break and continue statements to terminate or restart the loop when needed
'''

#Using the while True loop with a break statement
i = 0
while True: #The loop keeps on running infinite times
    print(i)
    if i == 10: #Check if the value of i = 10
        break #Terminate the infinite loop for i = 10
    i += 1 #Increment counter manually
    
#Using the while True loop with a continue statement (use of break is must in while True loops otherwise it will never terminate)
i = 0
count = 0
while True:
    if i == 10:
        break #Terminates the infinite loop if i = 10
    
    i += 1 #Increment counter manually
    
    if i % 2 == 0:
        continue #Sends the control flow of the loop back to the first line if the value of i is even
    else:
        print('{} is an odd number'.format(i)) #Displays the message if the number is odd
        
'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses While True Loop to compute the factorial of a number. Take a number from user with the prompt:

Enter an integer: ___________________ (Input comes in blank)

Once the input has been entered, the program should return the factorial of that number. An example would be:

Enter an integer: 7
Factorial of Inputted Number: 5040

'''
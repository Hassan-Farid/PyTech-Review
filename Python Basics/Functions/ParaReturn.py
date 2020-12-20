'''
    These functions are the ones that are mostly used as they make use of the arguments and return a value based on those arguments.
'''

def add_nums(a,b): #Takes two parameters as numbers
    return a + b #Returns the sum of the parameters so that it can be stored in a variable

#Calling the function
numSum = add_nums(2,3)
print("The sum of numbers provided to the function is: {}".format(numSum))

#Sometimes we need to display a message based on the value returned by a certain function
def check_even(num): #Takes one argument number
    if num % 2 == 0: #Checks if the number is even or not
        return True
    else:
        return False
    
num = int(input("Enter an integer: ")) 
if (check_even(num)): #Runs block of code if and only if check_even() returns True
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))
    
'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses a para return function, that uses a function to check if an argument passed is a palindrome or not.
Based on the return value, it should display the message whether or not it is. The output should look like this:

aabbcbbaa is a palindrome (Argument for the function: aabbcbbaa)

'''


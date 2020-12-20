'''
    Sometimes we need a default version of the arguments we define, this default value can be set when defining the function.
    This allows to pass that default value even if the user doesn't pass any arguments to the function
'''

#Adds two numbers and gives the result, if only one number is provided gives back the number as it is
def add_nums(a, b = 0):
    return a + b

#Calling the function
print(add_nums(2,3)) #With arguments
print(add_nums(2)) #Without second argument (default argument call)

#In case the default value is being stored as a variable value, we can have two cases:

#For immutable values such as variables or other immutable seqeunces, the variable value before the function definition is used as default
argval = 0

def add_nums(a, b = argval): #The value before function definition gets used as default value i.e. b = 0
    return a + b 

argval = 6 #This doesn't change the default value being used as the argument value

#Calling the Function
print(add_nums(2)) #Returns the value 2+0 = 2 instead of 2+1=3

#For mutable values such as lists or other mutable sequences, the variable value can be altered even after function definition
argval = [1,2,3]

def add_nums(a, b=argval): #Uses the reference of the array as the default value for the argument 
    return a + sum(b)

argval[0] = 5 #Change the first index item of array to 5

#Calling the function
#Now when function is called, the default argument value goes to the reference where the list is present and returns it
#Since the list has been altered, we get the new argument value as the default value
print(add_nums(2)) #Returns 2 + (5+2+3) = 12 instead of 2 + (1+2+3) = 8

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that takes two numbers as input from user and makes use of a function with default argument '+'.
Moreover, allow the function to only take '-', '*' and '/' as other inputs for the default argument. The program
will provide the result on the output based on the operation selected. An example of the program is:

Enter the first number: ______________________ (Input in the blank)
Enter the second number: _____________________ (Input in the blank)
Enter the operation you want to perform: ______________________ (Input in the blank)

Once the input has been provided, compute the result as:

Calculation: 2 + 3 = 5 (Default result)
Calculation: 4 - 3 = 1 (Argument: operator = '-')

'''
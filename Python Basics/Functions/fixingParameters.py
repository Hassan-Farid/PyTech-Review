'''
    Sometimes we need to contrain the use of positional or keyword arguments i.e. suppose we do not want a function call to be made with
    positional arguments or keyword arguments, then in such a case we make use of / and * in the arguments which have special meaning
    and put constarints on the use of positional and keyword arguments accordingly.
'''

#Creating a normal function (Can be called using both positional and keyword arguments)
def add_nums(a,b): #Takes two arguments which can be provided using both as positional or keyword
    return a + b

#Calling the function
print(add_nums(2,3)) #Takes two positional arguments
print(add_nums(a=2, b=3)) #Takes two keyword arguments
print(add_nums(2, b=3)) #Takes one positional argument and one keyword argument

#Creating a function with just positional argument calls (can be called only using positional arguments)
def add_nums(a, b, /): #All arguments before the argument / are turned to positional only by default
    return a + b

#Calling the function
print(add_nums(2,3)) #Takes two positional arguments (Returns the answer)
try: #Applying try and except as the function won't execute and will return a TypeError
    add_nums(a=2, b=3)
except TypeError as err:
    print("TypeError: {}".format(err))
    
#Creating a function with just keyword argument calls (can be called only using keyword arguments)
def add_nums(*, a, b): #All arguments after the argument * are turned to keyword only by default
    return a + b

#Calling the function
print(add_nums(a=2, b=3)) #Takes two keyword arguments (Returns the answer)
try: #Apply try and except as function won't execute and will return a TypeError
    add_nums(2,3)
except TypeError as err:
    print("TypeError: {}".format(err))
    
#Creating a function with all kinds of different parameter passing
def add_nums(a, /, b, *, c): #a = Positional-only, b = Standard(can be positional as well as keyword), c = Keyword-only
    return a + b + c

#Calling the function
print(add_nums(2, 3, c=4)) #For standard parameter as positional argument
print(add_nums(2, b=3, c=4)) #For standard parameter as keyword argument

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that uses a function, that takes three different types of arbitary arguments (positional, standard, keyword)
and returns the sum of averages of all the values entered

Execution of the function should give the result like:

Average of Arguments: 3.0 + 5.5 + 8.5 = 17.0 (positional: [1,2,3], standard: [4,5,6,7], keywords: [8,9])  

'''
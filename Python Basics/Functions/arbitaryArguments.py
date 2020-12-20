'''
    Sometimes a user wishes to enter as many arguments as he wants into the provided method
    This can be done using various methods, but the best method to perform this is using the built-in python * and ** operators
    * operator packs all the elements passed as arguments into a tuple so that operations can be performed easily on them.
    Similarly, ** operator packs all the elements passed as keyword arguments into a dictionary.
'''

def avgVals(*args): #Takes arbitary number of positional arguments (as a tuple)
    return sum(args)/len(args) #Returns the average of values in the tuple

#Calling the function
print(avgVals(1,2,3)) #Takes 3 arguments
print(avgVals(2,3,4,5,6,7,8)) #Takes 7 arguments
print(avgVals(1,2,3,4,5,6,7,8,9,10)) #Takes 10 arguments

def avgKeyVals(*args, **kwargs): #Takes arbitary number of positional as well as keyword arguments (as a tuple and dictionary respectively)
    kwSum = 0 #Initialize sum of dict values as 0
    for k, v in kwargs.items(): #Assign k = key  and v = value in (key, value) pair in kwargs dictionary
        kwSum += v #Adds the value to sum of values for each key
    return kwSum/len(kwargs) #Returns the average of the values summed

#Calling the function
print(avgKeyVals(a=1, b=2, c=3)) #Takes 3 keyword arguments
print(avgKeyVals(a=1, b=2, c=3, d=4, e=5, f=6)) #Takes 6 keyword arguments

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a program that checks whether the values for positional arguments and keyword arguments are same for the provided function.
Use arbitary amount of parameters to perform the task such that we have for the function with following arguments:

isequal_args_and_kwargs(2, 3, 4, a = 2, b = 3, c = 4)

We get the following result:

The provided arguments and keyword argument values are same.

'''
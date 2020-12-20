'''
    Sometimes we need to define the different data types that are needed for the parameters of the function.
    Moreover, the datatype of the value that is to be returned. These details are stored in the __annotations__ property of functions.
'''

#A simple function that takes two integer arguments and gives an integer return value
def add_sum(a: int, b: int) -> int:
    return a + b

#Displaying the annotations for the function (Returns a dicitonary of values)
print("Annotations: " + str(add_sum.__annotations__))

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a function that takes three arguments i.e. name, age and salary and display its function annotations

'''
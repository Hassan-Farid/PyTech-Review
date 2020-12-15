'''
    Sometimes while displaying messages, it is necessary to embedd variables yielded into a particular text
    For this we need to perform text formatting before displaying our messages
'''

#The most basic method of formatting text is using the printf statement
print(f'Hello World')

#This allows to embedd variables into text easily (Feature introduced in Python 3.6)
val = 5
print(f'The value to be displayed is {val}')

#This method also allows to use more than two fields for formatting
width = 15
height = 12
print(f'The width of the rectangle is {width} whereas its height is {height}')

#This method allows for nested formatting as well i.e. fields within fields
x = 2
y = 9
print(f'The point is located at the coordinates: {(x, y)}')

#Another alternative method for formatting text with variables is th format() method of the strings
num = 5
print('The value to be displayed is: {}'.format(num))

#The format method can take a list of arguments which are placed in the order in the text
#Thus if we have .format(arg1, arg2, arg3, ...) then the first {} will contain arg1, second {} will contain arg2 and so on
first = 2
second = 3
third = 4
print('This is first: {} , this is second: {} , this is third: {}'.format(first, second, third))

#A better way to place the list of arguments in the format into the placeholders is thus 
#using their number in which they are to be placed
width = 25
height = 10

#Since we have width as first argument it represents 0th position whereas height represents the 1st position
print('The width of the rectangle is {0} whereas its height is {1}'.format(width, height)) 

#The above statement can also be written as:
print('The width of the rectangle is {1} whereas its height is {0}'.format(height, width))

#Thus, the number of arguments in the placeholders allows flexibility in the code
#Additionally we can use different precision formats to limit the size in floating points but its optional

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Using variables assign the values shown in the message below and try to use format to display output of this format:

First point coordinates: (2, 5)
Second point coordinates: (7, 8)
The slope of the line through these points is given as follows:

    m = (y2 - y1)/(x2 - x1)
    m = (8 - 5)/(7 - 2)
    m = 3/5

which is the required slope of the provided coordinates
'''
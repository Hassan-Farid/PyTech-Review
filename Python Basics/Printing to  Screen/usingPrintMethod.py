'''
    The basic method of displaying messages on the screen is using the print() method
'''

#Using print() to display "Hello World" on the screen
print("Hello World")

#Using print() to display a variable value
val = 5
print(val)

#Using print() to display more than one strings as a list of arguments 
print("Hello", "World", "!")

#Using print() to display a combination of variable value and some text
print("The provided value to be displayed is: " , val) 

#The print method provides two arguments i.e. sep and end

#Using print statement with a seperator
print("Hello" , "World" , sep = ',') 

#Using print statement with a end argument
print("Hello", end=' ')
print("World")

#Using print statement with seperator and end argument
print("The", end = " ")
print("provided", end = " ")
print("value", end = " ")
print("to", end = " ")
print("display", end = " ")
print("is", end = " ")
print("", val, sep=": ")

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Print the following message in this format using the print method (you can use the arguments if needed):

This is me. 
My name is: Saleem (You can use your name here)
My father name is: Tipu (You can use your father name here)
My address is: ABC-XYZ Block Z House No 444 
My email address is: abc.123.def@gmail.com
I study at: IJK University
'''
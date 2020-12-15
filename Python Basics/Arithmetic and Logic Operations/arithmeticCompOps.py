'''
    Sometimes its needed to self increment or decrement something or apply an operation to the value already stored in a variable
    For such cases, it is essential to know the different handling of self-arithmetic operations
'''

#Assignment 
num = 5

#Using Self-Addition Operation
num += 3 #Equal to num = num + 3
print("New value of Number is {}".format(num))

#Using Self-Differencing Operation
num -= 4 #Equal to num = num - 3
print("New value of Number is {}".format(num))

#Using Self-Product Operation
num *= 3 #Equal to num = num * 3
print("New value of Number is {}".format(num))

#Using Self-Division Operation
num /= 4 #Equal to num = num / 4
print("New value of the number is {}".format(num))

#Using Self-Modulo Operation
num %= 2 #Equal to num = num % 2
print("New value of the number is {}".format(num))

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Take the following inputs by providing prompts to user:
    
Enter the temperature in Fahrenheit: ___________ (Input in the blank)

Once input has been taken, you can use print formatting to display ouput in the format: (Make use of self operations to convert F into C)

Temperature in Fahrenheit : 32 F
Equivalent Temperature in Celcius : 0 C

'''
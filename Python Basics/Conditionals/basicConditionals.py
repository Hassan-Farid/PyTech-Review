'''
    Conditionals are used to control the flow of execution of programs on basis of conditions
    Thua, it is essential that one should know how to apply these conditionals 
'''

#Using a single conditional 

#Assume we have to find whether a number is even or odd and print if it is even otherwise display no output
num = 4
if num % 2 == 0: #Checks whether the remainder of number/2 is 0 => Number is even 
    print("{} is Even".format(num))
    
# Using a double conditional

#Assume we have to find whether a number is even or odd and print the output according to the result
num = 5
if num % 2 == 0: #Checking for even number
    print("{} is Even Number".format(num))
else: #If not even then obviously its an odd number
    print("{} is Odd Number".format(num))
    
# Using more than two conditionals

#Assume we have to find whether a number is less than, equals to or greater than the other number and display the output accordingly
num1 = 10
num2 = 8
if num1 < num2:
    print("{0} is less than {1}".format(num1, num2))
elif num1 > num2:
    print("{0} is greater than {1}".format(num1, num2))
else:
    print("{} is equal to {}".format(num1, num2))

# Using two independent conditionals (Conditions that do not affect the result of one another)
marks = 87
if marks >= 85: #Condition to print A or A+ grade (Independent of whether one is passed or failed)
    print("You got a A or A+ grade")
if marks >= 50: #Condition to check if student passed exam (Dependent on the fact that the student didn't fail)
    print("You passed the Exam") 
else: #Condition to show that the student has failed (Dependent on the fact that the student didn't pass)
    print("You failed the Exam")

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Create a form validation program that takes an input as username and password from the user with prompts:

Enter Username: __________________ (Input Comes in Blank)
Enter Password: __________________ (Input Comes in Blank)

If the user enters the Username "ABC" and the Password "123" then we have the output:

Welcome! You have successfully logged in!

Otherwise, display the following output:

Incorrect Username (If only username is wrong)
Incorrect Password (If only password is wrong)
Incorrect Information (If both username and password are wrong)
'''
    
    
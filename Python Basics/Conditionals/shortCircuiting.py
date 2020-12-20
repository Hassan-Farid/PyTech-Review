'''
    In execution of multiple conditionals at the same time, it is necessary to apply short circuiting operations
    They allow to run a particular condition block code if both of them are satisfied or both of them are not satisfied
    It depends upon the case scenario. Nevertheless, it is essential for applying multi-condtional block of codes
'''

#Using the case scenario where both conditions are to be satisfied for execution (and operator)

#Consider the case that we have to check whether a number inputted is a multiple of 2 and 5
num = int(input("Enter an integer: "))
if (num % 2 == 0) and (num % 5 == 0):
    print("{} is a multiple of 2 and 5".format(num))
    
# Using the case scneario where either one of the conditions are to be satisfied for execution (or operator)

#Consider the case that we have to check whether a number inputted is a multiple of 2 or 5
num = int(input("Enter an integer: "))
if (num % 2 == 0) or (num % 5 == 0):
    print("{} is either divisible by 2 or by 5".format(num))
    
# Using the case scenario where the alternate condition is to be satisfied for execution (not oeprator)

#Consider the case that we have to check whether a number is odd or not
#We can use the alternative condition for an even number to check this
num = int(input("Enter an integer: "))
if not (num % 2 == 0):
    print("{} is an odd number".format(num))
    
# Now lets take a look at a case in which we can use all of these combined

#In a chemical processing plant, three liquid chemicals are used in the manufacturing process. Assume these chemicals are stored in 
#three different tanks with a level sensor attached to each tank. The level production of the product takes place with 70-75 ml of 
#first liquid, more than or equals to 35 ml of second liquid and less than 40 ml of the third liquid. In case any of the tanks gets to 15 ml the process sends
#a warning signal to a machine to refill the liquid in the tank, so that the process keeps going in continuation. 

#Now lets try to implement a program that works on the basis of the scenario defined above
firstLiquid = int(input("Enter the amount of liquid in first Tank: "))
secondLiquid = int(input("Enter the amount of liquid in second Tank: "))
thirdLiquid = int(input("Enter the amount of liquid in third Tank: "))

#Now checking whether all the amount of liquids in the tank are according to the requirements
if (firstLiquid == 0) or (secondLiquid == 0) or (thirdLiquid == 0): #Checking if tanks are empty
    print("Stopping Process.... The tanks are empty. Please refill them")
elif (firstLiquid <= 15) or (secondLiquid <= 15) or (thirdLiquid <= 15): #Checking if no tank is below 15ml
    print("Warning.... The tanks are running out of chemical. Please refill them")
elif (firstLiquid >= 70) and (secondLiquid >= 35): #Checking if the first Tank and second Tank are filled acc to requirements
    print("Great! The process requirements are all set. You can continue with the process")
elif not(firstLiquid >= 70): #Checking if first Tank does not satisfy requirement
    print("Requirements for the First Liquid are not satisfied. Please refill it")
elif not(secondLiquid >= 35): #Checking if second Tank does not satisfy requirement
    print("Requirements for the Second Liquid are not satisfied. Please refill it") 
else: #If none of the other case, then there must be some other error not specified in the requirements
    print("Some problem occured during the Process") 
    

'''
Task: Once done with this stuff, you can perform the following task to check if you got it or not

Consider a room temperature system that maintains the temperature of all the rooms in the banquet. The banquet comprises of 4 halls in total.
Hall 1 and 2 have a sub-system that checks the temperature of both halls is the same. Similarly there is another subsystem for halls 3 and 4.
There is a main system that checks whether the temperature of both sub-systems is same (Eventually leading to the result that the temp in
all the rooms is the same). Design a program that takes user input as:

Enter the temperature of Hall 1: __________________ (Input comes in blank)
Enter the temperature of Hall 2: __________________ (Input comes in blank)
Enter the temperature of Hall 3: __________________ (Input comes in blank)
Enter the temperature of Hall 4: __________________ (Input comes in blank)

Once input has been provided, use the given requirements to display the result the main system would give according to the input provided.
An example may be as follows:

Temperature of Hall 1: 78
Temperature of Hall 2: 78
Temperature of Hall 3: 78
Temperature of Hall 4: 69
The temperature for Subsystem 2 is not same. Please adjust the temperature accordingly.
'''
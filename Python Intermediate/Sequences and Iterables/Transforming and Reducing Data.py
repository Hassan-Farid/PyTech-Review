'''
    Assume you want to perform a aggregate function but on a filtered dataset
'''

#Suppose we are given a list of numbers and we want to compute the sum of squares of those numbers if they are odd
#We can achieve this by using the generator expressions

numList = [2,5,34,6,54,23,76,45,23]
oddSum = sum(x**2 for x in numList if x%2 != 0)

print(oddSum)

#Suppose we want to check whether there exists a .py file in the current directory
#We can make use of the os module to use the file managing methods

import os
dirFiles = os.listdir('D:\GitHub Repos\Python Scripts\Core Python\Sequences and Iterables')
if any(filename.endswith('.py') for filename in dirFiles):
    print('There is a python file here!')
else:
    print('No python file found in current directory')
    
#Suppose we have a tupe containing the student's name and his marks in maths and eng and we want to output it in .csv format
studInfo = ('Saleem', 97, 78)
print(','.join(str(x) for x in studInfo)) #Prints a comma seperated line which can then be written into a .csv file 

#Suppose we want to compute the lowest marks scored by the students in maths exams

studList = [
    {'name':'Hassan', 'marks':100},
    {'name':'Usman', 'marks':65},
    {'name':'Daniyal', 'marks':91},
    {'name':'Touseef','marks':76},
    {'name':'Adnan', 'marks':86},
    {'name':'Anas', 'marks':46}
]

minMarks = min(s['marks'] for s in studList)
print('The least marks scored by the students is: {}'.format(minMarks))


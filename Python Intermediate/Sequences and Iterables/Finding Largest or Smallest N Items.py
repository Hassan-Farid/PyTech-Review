'''
Assume we are given a certain list of items, we want to find the N largest/smallest items from that list
'''

#To find the N largest or smallest items in a particular list we can make use of the heapq module
#It provides us with the nlargest() and nsmallest() functions that allows to find the largest and smallest n items as used below

import heapq

#Consider a simple example of a list of marks obtained by the Students in the final exam that are provided 
#We want to find the highest three marks from this list

marks_list = [56,89,76,93,70,65,84,85,91,89,100]
print(heapq.nlargest(3,marks_list))

#Similarly for the lowest 3 marks in the class we have

print(heapq.nsmallest(3,marks_list))

#Now this seems a bit off, since there is no mentioning of who the student is
#Thus, we can instead take a list of dictionaries that contain the student name and the marks attribute
#Then we can apply these methods to get the proper result

student_marks = [
    {'name': 'Ali', 'marks': 56},
    {'name': 'Daniyal', 'marks': 89},
    {'name': 'Usman', 'marks': 76},
    {'name': 'Touseef', 'marks': 93},
    {'name': 'Adnan', 'marks': 70},
    {'name': 'Abdul Subhan', 'marks': 65},
    {'name': 'Ehsan', 'marks': 84},
    {'name': 'Moiz', 'marks': 85},
    {'name': 'Hasan', 'marks': 91},
    {'name': 'Hassan', 'marks': 89},
    {'name': 'Abdul Wahab', 'marks': 100},
]

#Using lambda function, we can apply the method to the marks attribute of the dictionaries in the list
print(heapq.nlargest(3, student_marks, key=lambda seq:seq['marks']))
print(heapq.nsmallest(3, student_marks, key=lambda seq:seq['marks']))


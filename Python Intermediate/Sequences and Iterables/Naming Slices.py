'''
Assume that we want to extract a certain slice from a particular long list
'''

#Suppose we are provided a large list with lots and lots of numbers and you want to get the sum of a particular bunch
#We can take a random list of numbers using the random.randint() method and then sum the specified slices

#Normally we can extract the slices by using compact numbers as indexes
from random import randint

random_list = []
for i in range(100):
    random_list.append(randint(0,100))
    
print(random_list)

#Suppose we want to sum up the slices yielded from the 40 to 50 indexes and 70 to 80 indexes
total = sum(random_list[40:50]) + sum(random_list[70:80])
print('The required total under given conditions is: {}'.format(total))

#Writing complicated slice indexes within the formula is little bit code complication
#To avoid this we can name the slices using the slice object and then use it in the formula 

first_slice = slice(40,50)
second_slice = slice(70,80)

newtotal = sum(random_list[first_slice]) + sum(random_list[second_slice])
print('The required total under given conditions is: {}'.format(newtotal))

#This slice object can be used wherever a slice is allowed i.e. strings, lists, ranges, etc.
#Suppose we are given a list of students final practical exams marks based on the project, with index of list representing their roll numbers
#Turns out that the roll numbers from 12 to 15 have been assigned the wrong marks and they are to be adjusted 

studMarks = []
for i in range(50):
    studMarks.append(randint(20,100))
    
print('The marks obtained by the respective 50 students are: {}'.format(studMarks) )    
    
#Now we want to adjust the marks of students from 12-15 in accordance with the adjusted marks list
adjustList = [67,78,91]
adjustSlice = slice(12,15)
studMarks[adjustSlice] = adjustList

print('The marks after adjusting obtained by the respective 50 students are: {}'.format(studMarks))

#The teacher found out that even though the marks were assigned to the students, the last 10 students were not under her consideration
#And their projects had to be judged by some other teacher so they would have to be removed from the given list

removeSlice = slice(40,50)
del studMarks[removeSlice] 
print('The marks after removing obtained by the respective 40 students are: {}'.format(studMarks))
print(len(studMarks))

#Suppose the teacher only wants to display the marks obtained by the students with even roll number from 16-32
#For such a case we need to provide the slice method with three parameters, the third one being the gap in slice 
#Using the indices() method for a slice object we can get the required result as displayed
selectSlice = slice(16,33,2)
for i in range(*selectSlice.indices(len(studMarks))):
    print(studMarks[i])
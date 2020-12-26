'''
Assume you want to apply functions on items stored in a dictionary such as finding maximum value, minimum value or sort the data
'''

#In case of applying operations on the dictionary items, it is better to apply the zip method on them first 
#The zip method allows to create a tuple iterable out of the elements of another sequence or iterable
#Lets consider a dictionary containing the name of students as keys and their obtained marks as the value

marksDict = {
    'Wahab': 100,
    'Adnan':76,
    'Touseef':91,
    'Usman':82,
    'Moiz':65,
    'Daniyal':95
}

#Now if we want to find the student with the minimum marks
minMarks = min(zip(marksDict.values(), marksDict.keys()))
print(minMarks)

#Now if we want to find the student with the maximum marks
maxMarks = max(zip(marksDict.values(), marksDict.keys()))
print(maxMarks)

#Now if we want to sort the students from the highest marks to the lowest 
marks_sorted = sorted(zip(marksDict.values(), marksDict.keys()))
print(marks_sorted)

#The only tradeoff of using the zip method is that it can be used only once for a certain method
#i.e. we cannot call the max and min methods on the same iterable created using a single zip method

#In case of duplicate values for the keys the zip method prioritizes the iterable with the higher key value
exDict = {
    'first':20,
    'last':50
}

dupminMarks = min(zip(exDict.values(), exDict.keys()))
print(dupminMarks)

#Another approach to solve this problem but a little inefficient then this is to use the lambda expression 

#For minimum marks we have
altminMarks = marksDict[min(marksDict, key = lambda k: marksDict[k])] 
print ('{}:{}'.format(min(marksDict, key = lambda k: marksDict[k]),altminMarks))

#For maximum marks we have
altmaxMarks = marksDict[max(marksDict, key = lambda k: marksDict[k])]
print('{}:{}'.format(max(marksDict, key = lambda k: marksDict[k]), altmaxMarks))



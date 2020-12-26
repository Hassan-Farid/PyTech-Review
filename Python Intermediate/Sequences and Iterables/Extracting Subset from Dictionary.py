'''
    Assume you want to create a dictionray as a subset from another dictionary based on some criteria
'''

#Suppose an institute has a record of all the students and their respective marks obtained in Maths subject
#The institute has a passing criteria for the exam that only those students with marks above 60 will be passed
#Based on this criteria, we can use the following to get the passing students from the provided set of students record

studMarks = {
    'Abdul Wahab': 50,
    'Hassan': 99,
    'Darain': 69,
    'Daniyal': 95,
    'Ehsan': 74,
    'Usman': 25,
    'Hasan': 81,
    'Touseef': 12,
    'Anas': 45
}

#Now to extract all those students with mark greater than or equal to 60
passStud = { key: value for key, value in studMarks.items() if value >= 60} 

#The method of creating such a dictionary using a certain criteria from another sequence is termed "Dictionary Comprehension"
print(passStud)


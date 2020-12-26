'''
Assume you want to sort a list of dictionaries with one or more of its keys
'''

#Suppose an institute conducts a test based on Maths and English marks and assigns positions to students based on their marks in these two subjects
#Suppose we are provided a list containing the json data for the students and the marks they obtained in subjects of English and Maths

studMarks = [
    {'name':'Touseef', 'maths':85, 'eng':82},
    {'name':'Darain', 'maths':91, 'eng':75},
    {'name':'Hassan', 'maths':100, 'eng':71},
    {'name':'Usman', 'maths':68, 'eng':83},
    {'name':'Daniyal', 'maths':95, 'eng':95}
]

#Now to sort the dictionary based on the common key values we can use the itemgetter class from the built-in operator module
from operator import itemgetter

#Lets sort the names based on the marks obtained in Maths (in descending order)
pos_by_maths = sorted(studMarks, key=itemgetter('maths'), reverse=True)
print(pos_by_maths)

#Let sort the names based on the marks obtained in English (in descending order)
pos_by_eng = sorted(studMarks, key=itemgetter('eng'), reverse=True)
print(pos_by_eng)

#Since the exam need to position the students based on overall marks from both Maths and English (in descending order)
pos = sorted(studMarks, key=itemgetter('maths','eng'))
print(pos)



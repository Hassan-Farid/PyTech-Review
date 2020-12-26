'''
Assume you create your own class with no native sorting support and you want to sort the objects created using that Class
'''

#Suppose that the institute needs to sort the student objects created using their Student Class
#The Student Class comprises of the student's name, their marks in maths and their marks in eng

class Student:
    def __init__(self, name, maths, eng):
        self.name = name
        self.maths = maths
        self.eng = eng
        
    def __repr__(self):
        return '(Name: {} , Maths: {} , Eng: {})'.format(self.name, self.maths, self.eng)
    
#Now creating a list of Students using the Student class
studMarks = [Student('Hassan', 100, 76), Student('Daniyal', 96, 91), Student('Darain', 89, 92), Student('Touseef', 85, 90)]

print(studMarks)

#Now sorting the elements of the list of student marks
import operator

pos_by_marks = sorted(studMarks, key = operator.attrgetter('name', 'maths', 'eng'))
print(pos_by_marks)

        
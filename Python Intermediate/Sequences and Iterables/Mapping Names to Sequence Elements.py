'''
    Assume you want to acess the elements of a sequence using a particular name instead of the index position
'''

#Suppose we are provided a sequence of elements and we want to access each field of that sequence with a certain name
#To perform such a task, we can use the collections.namedtuple() method as indicated

#Suppose a department has a list of attributes of a particular student i.e. his first name, last name, city, address and other information
#The department does not want to access data via the common indexes as its complicated but want a particular field of data by its field name

studInfo = ['Saleem', 'Aslam', 'saleem100100@gmail.com', '11-06-1996', 'Karachi', 'Pakistan', '0900-7680-1' , 'Computer Science']

from collections import namedtuple

#The above fields of the student can be indicated by the following field names to provide easy access
fieldnames = ['fname','lname','email','DoB','city','country','phone','dept']

#Now assigning these field names to the student
studTuple = namedtuple('StudentInfo', fieldnames)

#To pass the student Info list as arguments with each item representing a specific parameter we can use the star unpacking method
stud = studTuple(*studInfo)

#Now if we want to see the email address of the student, we can use:
print(stud.email)

#It should be noted that a named tuple is efficient than a dictionary
#The trade-off of this feature is that it is immutable in nature just like a normal tuple
#Thus, to change the field_names we can use a _replace() method

#Suppose the student whose data was mentioned above shifted to some place else e.g. Lahore
stud = stud._replace(city = 'Lahore') #_replace creates a new namedtuple with same attributes except the one to be replaced
print(stud.city)

#Another method of replacing data in a namedtuple is to provide a dictionary value containing all the attributes and convert it into a tuple
#The condition being that the number of fields in the named tuple be same as that in the dictionary
#This way we can populate all the data at once instead of doing it one by one

stud_prototype = studTuple('','','','','','','','') #Empty named tuple so its elements can be relaced

#Now we write a method to convert dictionary items into a named tuple
def dict_to_nmdtuple(newStud):
    return stud_prototype._replace(**newStud) #Double star unpacking unpacks the dict keys as well as values

#Now suppose a new student enters with the following information, we can create its named tuple as follows:
new_stud = dict_to_nmdtuple({'fname':'Shafiq', 'lname':'Hasan', 'email':'shafiqhasan@gamil.com', 'DoB':'07-02-1997',
                             'city':'Islamabad', 'country':'Pakistan', 'phone':'0123-45678-9', 'dept':'Mechanical'})

print(new_stud)
    



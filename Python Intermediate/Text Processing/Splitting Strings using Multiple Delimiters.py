'''
    Assume you want to access different substrings from a string based on multiple delimiters
'''

#Suppose a company is running a survey on the type of email patterns used by most users
#To find the possible email patterns it was suggested that all emails contain atleast one @ and .
#Other than that some users prefer to use numbers or dots within their username 

#Consider the following list of emails, gathered from a survey from 10 students
emailLists = [
    'abc.123@gmail.com',
    'def345@gmail.com',
    'ghi789@yahoo.com',
    'jklmno.546@gmail.com',
    'pqr78493@yahoo.com',
    'stuv.hello.235@hotmail.com',
    'xyz.pinocio.453.as_hero@yahoo.com'
]

#Now as per the given suggestion, the assigned demilters were as follows:
delimit_str = r'[.,_@]'

#To split the strings in the provided list based on delimiters we can use the re module
import re

userLenList = []
for email in emailLists:
    userLenList.append(len(re.split(delimit_str, email)) - 2) #Subtract 2 because the domain name comprises of mail server and top-level domain

#Now we can create a Counter class to count the number of occurences and store them in a dictionary
from collections import Counter

usernameCount = Counter(userLenList)
print('The most common format observed from the survey data is: {} username(s) within the specified delimiters'.format(usernameCount.most_common(1)[0][0]))

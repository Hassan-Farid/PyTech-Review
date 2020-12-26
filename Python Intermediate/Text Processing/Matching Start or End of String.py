'''
    Assume you want to find the string based on the starting or ending substring
'''

#Suppose a company gets a bunch of emails from its applicatnts
#Suppose when creating the form they forgot to put email pattern matching
#Thus, there may be a case that a wrong email format was submitted
#The form only approved the emails with .gmail or .yahoo domains

emailList = [
    'abc.123@gmail.com',
    'def345@gmail.com',
    'pqr78493@yahoo.com',
    'stuv.hello.235',
    'xyz.pinocio.453.as_hero@yahoo.com'
    'George',
    '',
    'ghi789@yahoo.com',
    'jklmno.546@gmail.com',
    'Email Address'
]

#Now to find the domain name, we can use the string.endswith() method on the following list of domains
validEmails = [email for email in emailList if email.endswith(('gmail.com', 'yahoo.com'))]
print(validEmails)

#Now suppose the same company surveyed a list of websites that the student developers most often visit
#For this they asked 10 students to fill out the website they visit the most for online community and/or problem solving
#It might be the case that some wrong web address is filled so a protection scheme for that was implemented

webAddrList = [
    'https://stackoverflow.com/questions',
    'file:///D:/Python/Python%20Core/Python_Cookbook_3rd_Edition.pdf',
    'https://github.com/',
    'http://docs.python.org/2/library/',
    'file:///D:/Python/Python%20Core/LearningPython%205e%202013.pdf',
    'https://stackoverflow.com/questions/tagged/python',
    'Github',
    'https://stackoverflow.com/questions/tagged/python',
    'Stackoverflow/Python',
    'https://www.reddit.com/r/Python/'
]

#Now the form allows only those web addresses that startwith 'http', 'https' or 'file' protocol

validWebAddr = [addr for addr in webAddrList if addr.startswith(('https','file','http'))]
print(validWebAddr)

#Moreover suppose that the company wants to view the contents of the address that is accessed the most
#We can use the Counter class to get the frequent occuring item and then use the urlopen method from urlib.request 

from urllib.request import urlopen
from collections import Counter

webAddrCount = Counter(validWebAddr)
#urlopen(webAddrCount.most_common(1)[0][0]).read() #Reads the html file structure of the file which can pe scrapped using Beautiful Soup library

#Another alternative but ineffecient method of yielding a string based on starting or ending substring is using slicing
sliceValidAddr = [addr for addr in webAddrList if addr[:5] == 'https' or addr[:4] == 'http' or addr[:4] == 'file']
print(sliceValidAddr)

#Yet another method to perform this task is using the python regex module re
import re

reValidAddr = [addr for addr in webAddrList if re.match('http|https|file', addr)]
print(reValidAddr)

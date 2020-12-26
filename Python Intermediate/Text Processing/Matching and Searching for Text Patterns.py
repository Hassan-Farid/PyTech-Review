'''
    Assume you want to search for a particular pattern in a string
'''

#Finding a simple string literal

#For simple strings we use built-in string methods such as str.find() or str.endswith(), etc.

#Assume we are provided a web addr name and we need to validate if its a https based web address with .com as the top-level domain
#We can use the basic string methods with AND operator to get the desired true or false value

webAddr = 'https://books.google.com'

if webAddr.startswith('https') and webAddr.endswith('.com'):
    print('{} is a valid address'.format(webAddr))
else:
    print('Could not validate the provided address')
    
#Now consider a more complicated search case

#Assume we are provided a web addr name and we need to validate if its either a http, https or ftp based address with either .com or .edu as top-level domain
#For such operations we can make use of the re module

import re

webAddr1 = 'https://stackoverflow.com'
webAddr2 = 'http://www.mit.edu'

if re.match(r'https|http|file[a-z0-9]com|edu', webAddr1):
    print('{} is a valid address'.format(webAddr1))
else:
    print('Could not validate the provided address')
    
if re.match(r'https|http|file[a-z0-9]com|edu', webAddr2):
    print('{} is a valid address'.format(webAddr2))
else:
    print('Could not validate the provided address')
    
#Now consider the case where you have to use the same particular matching pattern more than once
#We can use the re.compile() method to precompile the regular expression pattern for each search
#After compiling the pattern, we can use the match() method to match the pattern

webAddrList = [
    'https://stackoverflow.com',
    'http://www.mit.edu',
    'file://helloworld.pdf',
    'http://sadworld.com',
    'helloworld.py',
    'https://notopdomain',
    'file://noprotocol.edu'
]

#Now lloking for valid formats
validAddrList = []

pattern = re.compile(r'https|http|file[a-z0-9]com|edu')
for webAddr in webAddrList:
    if pattern.match(webAddr):
        validAddrList.append(webAddr)
            
print("The list of valid web addresses in the provided list is {}".format(validAddrList))

    


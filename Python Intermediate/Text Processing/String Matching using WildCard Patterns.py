'''
    Assume you want to match text using commonly used Unix wildcard characters
'''

#Suppose a company has a list of different file formats and they want to obtain only the ones with .csv in the end
#We can use the Unix wildcard pattern with the list of files using the fnmatch module
#fnmatch provides functionalities fnmatch() and fnmatchcase() which can help us in this task

from fnmatch import fnmatch, fnmatchcase

fileList = [
    'data.csv',
    'Test.html',
    'newdata.txt',
    'players.csv',
    'neat.CSV',
    'nice.txt',
    'scripts.py',
    'simple.py'
]

#Now we can use the basic expression '*.csv' to match whether the file is csv or not
for file in fileList:
    if fnmatch(file, '*.csv') == True:
        print(file)

#Although the above gives us the correct result, but assume that the company accepts lowercase extension files only
#In such case, we have to also look for the case instead of just string matching.

for file in fileList:
    if fnmatchcase(file, '*.csv') == True:
        print(file)
        
#As another example, lets assume we have been provided with a list of phone numbers belonging to Pakistani citizens
#As per the code 033- and the fact that the number is 11 digits long, we need to find all the numbers that use the Ufone SIM card

phoneList = [
    '03311111111',
    '03122222222',
    '03033333333',
    '0334444444444',
    '03455555555',
    '03266666666666',
    '902946656575676756',
    '03399999999',
    '03100000000'
] 

#Now checking for valid phone numbers and listing them
ufoneNumList = []

for phone in phoneList:
    if len(phone) == 11:
        if fnmatch(phone, '033*'):
            ufoneNumList.append(phone)
            
print('The valid Ufone Numbers in the provided list are: {}'.format(ufoneNumList))
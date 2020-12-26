'''
Assume you want to remove duplicates from a particular sequence
'''

#Consider the case of a hashable sequence (all immutable objects i.e. strings, tuples, etc.)
#For such a case we can make use of a set and a generator as indicated below

def rmv_hashduplicate(items):
    exist = set()
    for item in items:
        if item not in exist:
            yield item
            exist.add(item)
            
#Suppose the institute can offer atmost one student for a particular job
#Thus, we have to extract the unique jobs out of all the listed ones

jobList = ['FrontEnd','BackEnd','Desktop','Android','BackEnd','Data Analysis','BackEnd','FrontEnd','ML','Data Analysis']
print('The unqiue jobs offered in the jobList are: {}'.format(list(rmv_hashduplicate(jobList))))

#Now consider the case of unhashable sequence (e.g. dictionaries)
#For such a case we can add a certain code in case the items are unhashable sequences as well

def rmv_unhashduplicate(items, key=None): #keys argument can help in case the sequences provided are dictionaries
    exist = set()
    for item in items:
        itemval = item if key is None else key(item)
        if itemval not in exist:
            yield itemval
            exist.add(itemval)
            
#Suppose the institute can offer atmost one student for a particular job at a particular company

newjobList = [
    {'job':'FrontEnd', 'company':'Afiniti'},
    {'job':'BackEnd', 'company':'Folio3'},
    {'job':'FrontEnd', 'company':'10Pearls'},
    {'job':'Data Analysis', 'company':'Sys. Limited'},
    {'job':'BackEnd', 'company':'Folio3'},
    {'job':'Data Analysis', 'company':'10Pearls'}
]

print('The unique jobs being offered based on the given criteria are: {}'.format
      (list(rmv_unhashduplicate(newjobList, key=lambda k: (k['job'], k['company'])))))

#Now suppose we have to find unique jobs only from this particular list
print('The unique jobs being offered are {}'.format
      (list(rmv_unhashduplicate(newjobList, key=lambda k: k['job']))))

#Similarly in case of finding the unique companies offering the job
print('The unique companies offering the jobs are {}'.format
      (list(rmv_unhashduplicate(newjobList, key=lambda k: k['company']))))

#Another method avialable to remove duplicates is the by type converting the provided sequence into a set
#Since set is a collection of unqiue elements, thus the duplicates are removed bydefault
#The only disadvantage is that set does not preserve the order
#Lets apply the set method on the earlier provided jobList

print('The unqiue jobs offered in jobList are {}'.format(list(set(jobList))))

#In case of order preservence, the use of generator is a upvote as generators can also be used with files
#Consider a file with duplicate lines as indicated

with open('jobfile.txt', 'w') as dupfile:
    for job in jobList:
        dupfile.write('%s\n' % job)
        
#Now applying the function to search for the duplicates
with open('jobfile.txt') as jobfile:
    for line in rmv_unhashduplicate(jobfile):
        print(line)

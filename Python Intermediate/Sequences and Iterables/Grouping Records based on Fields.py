'''
Assume you have a certain number of sequences of dictionaries or sequences so as to group the items based on a particular field 
'''

#Consider a list consisting of a set of dicitonaries containing the students name and their college names from which they are applying
#The institute wants to group the students based on their institute they have come from

applyStud = [
    {'name':'Usman', 'colg':'Adamjee'},
    {'name':'Daniyal', 'colg':'DJ'},
    {'name':'Darain', 'colg':'Adamjee'},
    {'name':'Raza', 'colg':'Dehli'},
    {'name':'Hassan', 'colg':'Adamjee'},
    {'name':'Sameer', 'colg':'Dehli'},
    {'name':'Faraz', 'colg':'National'},
    {'name':'Areeb', 'colg':'DJ'}
]

#Now to group data based on the college name, we can use the groupby() method from the itertools
from operator import itemgetter
from itertools import groupby

#First lets sort the given data based on the required list i.e college
sortStud = sorted(applyStud, key = itemgetter('colg'))

#Now lets iterate through the sorted list based on the college attribute
for name, colg in groupby(sortStud, key = itemgetter('colg')):
    print(name)
    for i in colg:
        print(' ', i)
        
#Although this method works well but still if in case the sequence of dictionaries is not sorted
#Then we can not get the right type of groups from the records
#Thus, we can make use of defaultdict to create a multivalued dict containing multi values based on the college name

from collections import defaultdict
stud_by_colg = defaultdict(list)
for stud in applyStud:
    stud_by_colg[stud['colg']].append(stud)
    
#Now we can find each record for the College easily
print('\n Adamjee')
for col in stud_by_colg['Adamjee']:
    print(col)
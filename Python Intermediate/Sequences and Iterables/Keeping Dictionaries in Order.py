'''
Assume you want to create a dictionary that maintains the order in which values are inserted in the dictionary
'''

#An ordered Dicitonary is one that maintains the order in which elements are inserted 
#To obtain such a dictionary we can make use of the collections module which has a method OrderedDict
#This OrderedDict maintains the track of items added to the dicitonary in order using an internal doubly linked list

from collections import OrderedDict

d = OrderedDict()
d['First'] = 30
d['Second'] = 50
d['Third'] = 40
d['Fourth'] = 60

for key in d:
    print(key, d[key])
    
#The OrderedDict can be of major use when serializing or encoding data into some different format
#Suppose we want to control the ordering of the students and their respective marks to be serialized in a JSON format
#We can create an OrderedDict and then dump it into a JSON file

import json

new_d = OrderedDict()
new_d['Abdul Wahab'] = 100
new_d['Adnan'] = 76
new_d['Hasan'] = 81
new_d['Touseef'] = 92
new_d['Moiz'] = 70

print(json.dumps(new_d))
'''
Assume you want to create a dictionary object that maps keys to more than one values i.e. a Multivalued Dict
'''

#A dictionary object by default allows only one key to be assigned to a particular value at a time
#If one wants to add multiple values to a dictionary key, it will more probably be like

class MultivaluedDict():
    
    def __init__(self):
        self.dictionary = {}
        
    def createKey(self, key_pairs):    
        for key, values in key_pairs:
            if key not in self.dictionary:
                self.dictionary[key] = []
            self.dictionary[key].append(values)
            
    def __repr__(self):
        return '{}'.format(self.dictionary)
        
#Now running this function on a set of pair one by one
d = MultivaluedDict()
pairs = [('First', 30), ('Second',40), ('Third',50), ('First', 80), ('Third',70)]
d.createKey(pairs)
print(d)

#Although this is the correct method, there are alternate and more efficient ways to perform this task
#For instance, the Collections module provides us with a function defaultDict() that allows to create Multi-valued Dictionaries for properly

from collections import defaultdict

new_d = defaultdict(list)
new_d['First'].append(30)
new_d['Second'].append(50)
new_d['Third'].append(70)
new_d['First'].append(30)
new_d['Third'].append(70)

print(new_d)

#Another method we can use is the setdefault method on the normal dictionary object

newer_d = {}
newer_d.setdefault('First', []).append(30)
newer_d.setdefault('Second', []).append(50)
newer_d.setdefault('Third', []).append(70)
newer_d.setdefault('First', []).append(30)
newer_d.setdefault('Third', []).append(70)

print(newer_d)
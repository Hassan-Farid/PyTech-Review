'''
    Suppose you have to different dictionaries and you want to map them into a single dictionary 
'''

#Suppose we have dictionaries for two different sections of a class and their marks
#The institute wants to merge the dictionaries to create a single dicitonary to perform operations

secA = {'a':76, 'b':81, 'c':38, 'd':59}
secB = {'w':93, 'x':28, 'y':72, 'z':12}

#We can use collections.ChainMap() method to map these dictionaries into a single dictionary
from collections import ChainMap

classList = ChainMap(secA, secB)
print(classList)

#On displaying the classList we see that it does not create a merged dicitonary instead a list of dictionaries
#The speciality of the ChainMap() method is that it looks for the particular keys in all the dictionaries in the present list
print(classList['w'])

#All methods of dictionary work on the ChainMap data structure
print(len(classList))
print(list(classList.keys()))
print(list(classList.values()))

#ChainMap uses the original dictionaries hence updates itself when the dictionary is mutated
#Suppose it was found that the student c got 83 marks instead of 38, we have
secA['c'] = 83

print(classList['c'])

#An alternate method to map many mappings into a single mapping is by update() method of a dictionary
#It creates a new dictionary and stores the keys and values of the mappings in it
#Drawback of this method is that it does not update with the mutation in the original dictionary
merged_dict = dict(secB)
merged_dict.update(secA)
print(merged_dict)



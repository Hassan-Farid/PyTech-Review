'''
Assume you are provided a sequence and you want to find the most occuring value in that sequence
'''

#Suppose you are provided with a list containing the languages selected by various programmers that they use the most
#You want to compute the top three languages that stands out among the ones gathered from your sample 

#The list for the languages gathered is as follows
langList = ['Python','Java','Javascript','C#','Dart','Python','Javascript','Javascript','Python','C#',
            'C++','Java','Javascript','Python','Javascript','Javascript','Ruby','C#','C#','Javascript',
            'Ruby','C++','Python','Javascript','Java','Python','Javascript','C#','C++','Java']

#For this purpose we can use the collections.Counter.most_common() method
from collections import Counter

lang_count = Counter(langList)
topLangsCount = lang_count.most_common(3)
topLangs = []

for langCount in topLangsCount:
    topLangs.append(langCount[0])
    
print('The top three languages from the gathered sample are: {}'.format(topLangs))

#Suppose we take another sample from 10 more programmers and want to add the count of those samples into the already calculated one
#We can perform this using the update method on the lang_count Counter object

newlangList = ['Python','C#','Javascript','Python','Python','Java','C++','Java','Java','Python']
lang_count.update(newlangList)
newtopLangsCount = lang_count.most_common(3)
newtopLangs = []

for newlangCount in newtopLangsCount:
    newtopLangs.append(newlangCount[0])

print('The top three languages from the newly gathered sample are: {}'.format(newtopLangs))

#Now suppose the obtained sample was from programmers from both Karachi and Lahore
#We want the count of only the three most used languages in Karachi
#For such a case we are provided a list of languages that were selected by devs in Lahore and need to remove it from obtained new sample

rmvlangList = ['Python','C#','Javascript','Java','Java','C#','C++','Ruby','Python','Javascript','Python','Java']
rmvlang_count = Counter(rmvlangList)

#To remove the count we can use the set difference operation 
updlang_count = lang_count - rmvlang_count
updtopLangsCount = updlang_count.most_common(3)
updtopLangs = []

for updlangCount in updtopLangsCount:
    updtopLangs.append(updlangCount[0])
    
print('The top three languages from the sample taken from Karachi are: {}'.format(updtopLangs))







 
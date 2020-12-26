'''
    Assume you are provided an iterable and you want to process it manually instead of with for loops
'''

#Suppose we are provided a list of values and we want to traverse through it, display the name of each item in that list
#We can use the next() function to consume an iterator manually as shown in the example below

#First create a file object and store data in it
itemList = [
    'apple',
    'banana',
    'orange',
    'pear',
    'grapes',
    'jackfruit',
    'watermelon'
]


with open('newfile.txt', 'w+') as f:
    for item in itemList:
        f.write('%s \n' % item)

#Now creating a manual iterator for the list
def manualIterator(iterator):
    try:
        while True:
            item = next(iterator)
            print(item)
    except StopIteration:
        pass
    
#Now lets read elements from the file one by one using our manually created iterator
with open('newfile.txt') as file:
    manualIterator(file)
    
#We can also use the iter() function to convert any sequence or iterable into an iterator
iterItemList = iter(itemList)
manualIterator(iterItemList)

#Although this is a manual implementation of the for loop, it is actually the mechanics on the basis of which the for loop works

    

'''
    Assume you want to create an iterator that iterates the values of sequence in reverse order
'''

#To iterate in reverse on a sequence we can use the built-in reversed() method

#Suppose we want to create a Countdown class with a trigger
#The trigger can be called which decrements the values as well as increments 

class Countdown:
    
    def __init__(self, start):
        self.start= start
        
    #Creating a forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
            
    #Creating a reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
            
if __name__ == "__main__":
    counter = Countdown(5)
    
    #For decrement counter
    for x in counter:
        print(x)
        
    print("==============")
        
    #For increment counter
    for x in reversed(counter):
        print(x)
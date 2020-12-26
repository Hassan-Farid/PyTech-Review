'''
    Assume you want to create your own iteration pattern like range()
'''

#Suppose we want to create a pattern that increases floating point by a certain floating point offset
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment
        
#Now applying the created iteration pattern
if __name__ == "__main__":
    floatList = []
    for num in frange(0.5, 5, 0.6): #Initializes the num value from 0.5 and increments 0.6 for each iteration
        floatList.append(num)
        
    print(floatList)
    
#The yield operation in the given function returns a generator which in turn works on the basis of iterations only
'''
    Assume you want to create an iterator container that can consume iterables within it self as child iterator containers
'''

#Suppose we want to create a family tree e.g. using the name of a person we can list his sons
#To do that we can make use of the __iter()__ method

class IterContainer:
    
    def __init__(self, value):
        self.value = value
        self._children = []
        
    def __repr__(self):
        return '{}'.format(self.value)
    
    def add_child(self, iterator):
        self._children.append(iterator)
        
    def __iter__(self):
        return iter(self._children)
    
#Now lets apply the iterContainer for a certain parent 'A' having children 'B' and 'C'

if __name__ == "__main__":
    parent = IterContainer('A')
    child1 = IterContainer('B')
    child2 = IterContainer('C')
    
    #Adding children to the parent iter container 
    parent.add_child(child1)
    parent.add_child(child2)
    
    #Displaying the children for a given parent using for loop iterator
    for child in parent:
        print('{} is a child of parent {}'.format(child, parent.value))
    
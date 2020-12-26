'''
Assume you want to implement a priority queue that sorts items in a queue based on their priority
'''

#A priority queue is an ADT similar to a queue which functions the same way as a queue (FIFO order) but pops/deques elements based on priority

#We will now create a class PriorityQueue and use another class Marks to insert marks into the Queue so that they can be dequeued with priority
#We use the heapq module to implement the following mentioned above

import heapq

class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0
    
    #Push would require a certain priority integer value which would represent the order in which the students have to be dequeued 
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
        
    #Pop would remove a value from the queue like a normal pop using the FIFO method
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Marks():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def __repr__(self):
        return '{} has {} marks'.format(self.name, self.marks)
    
#Now lets use the priority queue by pushing the Students and their Marks and then popping them out

if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Marks('Touseef', 86), 86)
    q.push(Marks('Hasan', 79), 79)
    q.push(Marks('Adnan', 89), 89)
    q.push(Marks('Moiz', 69), 69)
    q.push(Marks('Abdul Wahab', 100), 100)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
        
#As we can see from the result, the student with the lowest priority was popped out first and the student with the highest priority
#was popped out last
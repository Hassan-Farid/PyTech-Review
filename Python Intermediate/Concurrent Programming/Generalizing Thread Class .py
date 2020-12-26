'''
    Assume you want to override methods in the Thread class to create your new Thread based Class
'''

#Suppose that we want to create a Countdown Thread class by overriding the methods in the built-in Thread class
from threading import Thread
import time

#Remember that we can only override the __init__() and run() method 
class CountdownThread(Thread):
    
    def __init__(self, n):
        super().__init__()
        self.n = n
        
    def run(self):
        while self.n > 0:
            print('Counter value: ' , self.n)
            self.n -= 1
            time.sleep(2)
    
c = CountdownThread(10) #Creates a thread based counter till 10
c.start() #Since the class is inherited from Thread thus it carries all of its functionalities

#The only trade-off this method in comparison to creating a Thread class and using it in your code
#Is that it introduces an extra dependency which results in a class that can only be used with context of threads 

        
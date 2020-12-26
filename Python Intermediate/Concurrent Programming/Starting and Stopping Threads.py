'''
    This script allows you to manage activities regarding the creation of threads
'''

#Python provides a built-in class threading.Thread() 
#This class can be overridden based on two methods i.e. either __init__() or run() method

#The Thread method creates a thread instance 
#The threading library allows any callable to execute itself in its own thread

#Lets create a simple function using the time module to run a counter with some time delay
import time

def countdown(n):
    while n > 0:
        print('Counter value: ', n)
        n -= 1
        time.sleep(2) #Delays the loop for 2 seconds after each count
        
#Now for creating a thread instance
from threading import Thread
t = Thread(target = countdown, args=(10,))

#When a thread instance is created, it doesn't invoke on its own instead we have to use the start method
t.start()

#To make sure that the thread is still active or not, we can use the isalive() method
if t.is_alive():
    print('\nThread is still running')
else:
    print('\nThread has stopped')
    
#In case of a very long running thread or a background running thread we use the Daemon attribute
#Daemon threads are background processes which keep the main thread running and are destroyed automatically as soon as the main thread ends

new_t = Thread(target = countdown, args=(20,), daemon=True)
new_t.start() #We will see that the execution of the thread stops as soon as the main thread t terminates

#Although the thread keeps running until its target is achieved, but sometimes we want to stop it at some selected points
#To do that, we need to create our own class and define the selected points as to where the thread must stop

#For that purpose lets create a Counter class
class CountdownProcess:
    
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self, n):
        while self._running and n > 0:
            print('Class implemented Counter value: ', n)
            n -= 1
            time.sleep(2)
            
#The above class is the exact implementation of the countdown function but with an overridden run() method
#We can pass this method as value to the target parameter 
c = CountdownProcess()
newer_t = Thread(target = c.run, args=(10,))
newer_t.start()
time.sleep(8)
c.terminate() #We want to  terminate the thread after 8 seconds have passed
t.join()




    


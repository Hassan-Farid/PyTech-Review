'''
Assume we are given a certain sequence and want to keep the last N elements from it 
'''

#Application of a such a script comes in case you have a certain amount of history data on your browser
#You want to remove all the history data exxcept the last 3 links with the keyword 'OpenCV'
#We consider the scenario using a file with contents stored as history data and then use an approach to save the last 3 links only

from collections import deque

#First we can create a file and store the link contents in it

links = [
    "https://opencv.org/",
    "https://www.google.com/",
    "https://stackoverflow.com/questions/tagged/opencv",
    "https://stackoverflow.com/questions/64713179/adjust-brightness-and-contrast-opencv-c",
    "https://www.udemy.com/topic/opencv/",
    "https://www.wikipedia.org/",
]

with open('newfile.txt', 'w') as f:
    for link in links:
        f.write("%s\n" % link)   
        
#Now we can write a method that will allow us to search for the last N = 3 links with the keyword "OpenCV" in them
def search_links(links, keyword, num=3):
    required_links = deque(maxlen = num) #collections.deque allows to create a queue that inserts value and removes them using FIFO if the queue gets full
    for link in links:
        if keyword in link:
            yield link, required_links
            required_links.append(link)
        
#Now we can use this method in our main function call to get the last 3 links related to OpenCV
if __name__ == "__main__":
    with open('newfile.txt') as f:
        for link, required_links in search_links(f, 'opencv'):
            for links in required_links:
                print(links, end='')
            print('-' * 20)
        
#We will get the output of the form as shown below, which shows the links that were accessed the last time with the 'opencv' in them
#(Note first entry in the file corresponds to the last entry in the list as the history in the browsers work in a similar manner
# i.e. when a particular link is accessed it gets written into the history log file after which the next link is appended to that log file 
# and so on. Similarly, the first record in the provided file would be the last one accessed by the users hence giving us the last three 
# links with the keyword 'OpenCV' in them)

'''
--------------------
https://opencv.org/
--------------------
https://opencv.org/
https://stackoverflow.com/questions/tagged/opencv
--------------------
https://opencv.org/
https://stackoverflow.com/questions/tagged/opencv
https://stackoverflow.com/questions/64713179/adjust-brightness-and-contrast-opencv-c
--------------------
'''        


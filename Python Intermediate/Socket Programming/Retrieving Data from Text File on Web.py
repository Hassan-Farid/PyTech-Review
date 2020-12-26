'''
    Assume there is a text file somewehere on the Web and you want to retrieve its details
'''

#Suppose we want to extract the details of a file named "intro-short.txt" on the web address "http://data.pr4e.org/"
#We can use a GET request on port 80 and use socket connection to retrieve the information

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#Prininting the data on the screen
while True:
    data = mysock.recv(512) #512 characters retrieval per loop
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
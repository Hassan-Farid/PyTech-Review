'''
    Assume you are given a json document and want to extract data from it to get your particular information
'''

#Suppose a XML document was recieved by a company containing the names and votes of people who were surveyed for rating json language out of 100
#The company wants to extract the number of these counts and conclude the percentage of the votes in favour of the language
#Moreover they need to find the total number of characters recieved in the form of strings on file transfer

#Importing necessary libraries
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#A simple method that uses indexing to extract data from the name and count tags
def jsonRetriever(url):
    
    if len(url) < 1:
        return 
    
    jsonData = urllib.request.urlopen(url).read()
    jsonInfo = json.loads(jsonData.decode())
    
    nameStr = ''
    numList = []
    
    for x in jsonInfo['comments']:
        nameStr = nameStr + x['name']
        numList.append(int(x['count']))
        
    return nameStr, numList
  
#Running the program for the provided file  
if __name__ == "__main__":
    url = input('Enter address: ')
    
    nameStr, numList = jsonRetriever(url)
    print('Retrieved {} characters'.format(len(nameStr)))
    print('Count: {}'.format(len(numList)))
    print('Sum: {}'.format(sum(numList)))
    

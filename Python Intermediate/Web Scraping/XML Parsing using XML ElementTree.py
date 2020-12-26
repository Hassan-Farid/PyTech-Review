'''
    Assume you are given a XML document and want to parse it to get your particular information
'''

#Suppose a XML document was recieved by a company containing the names and votes of people who were surveyed for rating XML language out of 100
#The company wants to extract the number of these counts and conclude the percentage of the votes in favour of the language
#Moreover they need to find the total number of characters recieved in the form of strings on file transfer

#Importing necessary libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#A simple method that uses XPath Selector to extract data from the name and count tags
def xmlParser(url):
    if len(url) < 1:
        return 
    
    xmlData = urllib.request.urlopen(url).read()
    
    xmlTree = ET.fromstring(xmlData)
    
    nameString = ''.join(x.text for x in xmlTree.findall('.//name'))
    countList = [int(x.text) for x in xmlTree.findall('.//count')]
    
    return nameString, countList
    
#Running the program for the provided file
if __name__ == "__main__":
    addr = input('Enter location of XML file: ')
    
    nameString, countList = xmlParser(addr)
    print('Retrieved {} characters'.format(len(nameString)))
    print('Count: {}'.format(len(countList)))
    print('Sum of Numbers: {}'.format(sum(countList)))
    
'''
    Assume we want to extract the text from particular tags in a HTML file 
'''

#Python has a third-party library known as Beautiful Soup that allows to parse HTML files easily
#The returned result is then treated just like a html file and text from multiple tags can be retrieved easily 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter the URL to scrape for text
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')

#Suppose the provided text in the span tags are numbers whose sum is to be computed
numList = []
for tag in tags:
    numList.append(int(tag.text))

print(sum(numList))
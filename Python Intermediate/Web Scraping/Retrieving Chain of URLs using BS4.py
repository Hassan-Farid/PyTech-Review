'''
    Assume you are provided a URL which contains a list of URLS. This script allows to open the Nth URL within a URL M Times recursively
'''

#Suppose we are provided a URL which contains a list of many URLs
#It is found that the contents of each URL in the list comprises of yet another list of URLs and so on
#It is wished to get the URL at the Nth Position within the list of URLs after retrieving the contents M times 

#Importing necessary modules
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#This function allows to retrieve URL recursively until the provided count of times is reached
def urlRetrieve(url,count,pos):

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a') #We get the anchor tag as it comprises of the ref to the url 
    tag = tags[pos - 1]
    if count == 1:
        return tag.get('href', None)
    else:
        return urlRetrieve(tag.get('href', None), count-1, pos) #Recursive callable until count reaches the desired count
        
#Now executing the above function
if __name__ == "__main__":
    url = input('Enter url:')
    count = int(input('Enter count:'))
    position = int(input('Enter position:'))
    
    resultUrl = urlRetrieve(url, count, position)
    print(resultUrl)
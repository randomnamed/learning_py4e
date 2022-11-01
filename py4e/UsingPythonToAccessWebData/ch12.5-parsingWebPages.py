#Web Scraping
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
# http://www.dr-chuck.com/page1.html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
# tags = soup('h1')
# for tag in tags:
#     print(tag.content)

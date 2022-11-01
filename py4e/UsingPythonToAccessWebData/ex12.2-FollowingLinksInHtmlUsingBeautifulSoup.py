# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
print('Retrieving: ', url)


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for c in range(count):
    i = 0
    for tag in tags:
        i = i + 1
        if i == position:
            save = tag.get('href', None)
            print('Retrieving: ', save)
            html = urllib.request.urlopen(save, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            break
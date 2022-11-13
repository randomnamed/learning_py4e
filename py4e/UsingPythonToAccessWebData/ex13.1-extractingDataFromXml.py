import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) > 1: 

    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    converted = data.decode()
    #print(converted)
    tree = ET.fromstring(converted)

    lst = tree.findall('comments/comment')
    print('Count:', len(lst))
    sum = 0
    for item in lst:
        #print(item)
        value = int(item.find('count').text)
        sum = sum + value
        
    print('Sum:', sum)
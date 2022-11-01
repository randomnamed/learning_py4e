# American Standard Code for Information Interchange
# ord function tells us numeric value of a simple ASCII character
print(ord('H'))
print(ord('e'))
print(ord('\n'))
#unicode or Ascii are all string in py3
x = 'sifn'
print(type(x))
x = u'sifnsoan'
print(type(x))
#byte string
x = b'aomdk'
print(type(x))


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# bytes = encode strings (assumes UTF8)
mysock.send(cmd)

#decode data when data read from external resource
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode() 
    # Unicode String  = Decode UFT8 or ASCII
    print(mystring)
mysock.close()
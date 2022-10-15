import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect( ('data.pr4e.org', 80) )
                    #Host          Port
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# .encode command converts unicode to Utf8
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysocket.close()
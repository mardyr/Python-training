import socket

my_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # informacje wysylane sa w UTF-8 , a tutaj sa w unicodzie , wiec enkodujemy na UTF-8
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if(len(data)<1):
        break
    print(data.decode()) # A TU DEKODUJEMY NA UNICODE
my_sock.close()

import urllib.request,urllib.parse,urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print(counts)

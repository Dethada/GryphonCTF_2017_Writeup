#!/usr/bin/python
import socket

server = "prog.chal.gryphonctf.com"
port = 17451

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting to {}:{}...".format(server, port)

s.connect((server, port))
result = s.recv(4096).decode("UTF-8")
print result
print "-"*20
s.send(str("\r").encode())

while True:
    result = s.recv(4096).decode("UTF-8")
    print result
    fk = list(result)
    idk = ""
    for i, j in enumerate(fk):
        if j == "\x1b":
            idk += j + fk[i+1] + fk[i+2] + fk[i+3]
            break
    x = [u'\x1b', u'[', u'9', u'2'] # Green

    if list(idk) == x:
        s.send(str("Yes! I will study").encode())
    else:
        s.send(str("No! I won't study").encode())

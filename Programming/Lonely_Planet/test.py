#!/usr/bin/python
from pwn import *

c = remote("prog.chal.gryphonctf.com",  17453)
reply = c.recv(timeout=10)
print reply
check = set(["English", "Alphabetrium", "Gazorpazorpian", "Numberconian", "Martian", "Unition", "Blitzion", "Chipzion", "Morphian"])
reply = reply.splitlines()
length = len(reply) -1
line1 = reply[length-1].split(" ")
line2 = reply[length].split(" ")
origiLang = ""
lang = ""
text = []
for j,i in enumerate(line1):
    if i in check:
        origiLang = i
    elif i == ":":
        for x in range(j+1, len(line1)-1):
            text.append(line1[x])

for i in line2:
    if i in check:
        lang = i
        break
print origiLang
print lang

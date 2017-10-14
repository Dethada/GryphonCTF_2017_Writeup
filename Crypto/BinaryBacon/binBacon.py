#!/usr/bin/python
import sys, binascii

f = open("BACON.txt", 'r')
f_contents = f.readlines()
linez = []
for i in f_contents:
    linez.append(i.rstrip('\r\n'))
f.close()

f = open("BINARY.txt", 'r')
f_contents = f.readlines()
tmp2 = []
for i in f_contents:
    tmp2.append(i.rstrip('\r\n'))
keyz = []
for line in tmp2:
    keyz.append(line.split(" : "))
answer = ""
for pair in keyz:
    x = ord(linez[int(pair[0])-1][int(pair[1])-1])
    if  x > 64 and x < 91:
        answer += '1'
    else:
        answer += '0'

print binascii.b2a_uu(answer)

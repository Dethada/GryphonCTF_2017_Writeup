#!/usr/bin/python
import binascii
import base64

f = open("hiddenflag")
f_contents = f.read()

tmp = f_contents
ans = ""

def solve(s):
    bin1 = int(s, 2)
    b64 = binascii.unhexlify('%x' % bin1)
    return base64.b64decode(b64)

while '{' not in tmp:
    tmp = solve(tmp)

print tmp

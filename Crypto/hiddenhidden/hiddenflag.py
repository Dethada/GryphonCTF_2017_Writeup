#!/usr/bin/python
import binascii, base64

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

fileName = "Crypto Hotdogs\\hiddenflag"
f = open(fileName, 'r')
f_contents = f.read()
x = chunkstring(f_contents, 8)
text = ""
fk = ""
# hexed = hex(int(f_contents, 2))
for j in x:
    try:
        text += ''.join(chr(int(j[i:i+8], 2)) for i in xrange(0, len(j), 8))
    except ValueError:
        fk += j
# characters = set(['A', 'E', 'D', 'M', 'T', 'w', 'x'])
decoded = base64.b64decode(text)
hexed = hex(int(decoded, 2))
print len(hexed)

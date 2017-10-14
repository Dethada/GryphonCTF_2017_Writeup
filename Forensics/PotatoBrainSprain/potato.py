#!/usr/bin/python

fileName = "Forensics/Potatos_Brain.txt"
f = open(fileName, 'r')
f_contents = f.readlines()
tmp = []
for i in f_contents:
	tmp.append(i.rstrip('\r\n'))
bf = set(['<', '>', '+', '-', '.', ',', '[', ']'])
coded = ""
for line in tmp:
    for char in line:
        if char in bf:
            coded += char

print coded

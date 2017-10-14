#!/usr/bin/python
import hashlib, random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
count = 0

while count < 20:
    length = random.randint(5, 20)
    combi = ""
    for i in range(length):
        combi += random.choice(letters)
    hash = hashlib.sha512(combi).hexdigest()
    if hash[:2] == "00":
        count += 1
        print "{}. {}".format(count, combi)

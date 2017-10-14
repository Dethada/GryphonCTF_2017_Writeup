#!/usr/bin/python
from Languages import *
from pwn import *
import sys

check = set(["English", "Alphabetrium", "Gazorpazorpian", "Numberconian", "Martian", "Unition", "Blitzion", "Chipzion", "Morphian"])
f = open("Translation.txt", "r")
f_contents = f.readlines()
words = []
for line in f_contents:
    words.append(line.rstrip('\r\n').split(" -> "))
dictionaryz = [] # 962 words baby
for line in words:
    dictionaryz.append(Language(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
print "[*] Dictionary loaded"

def translateMe(origiLang, lang, w):
    if origiLang == "English":
        for word in dictionaryz:
            if word.English == w:
                return word.translate(lang)
    elif origiLang == "Alphabetrium":
        for word in dictionaryz:
            if word.Alphabetrium == w:
                return word.translate(lang)
    elif origiLang == "Gazorpazorpian":
        for word in dictionaryz:
            if word.Gazorpazorpian == w:
                return word.translate(lang)
    elif origiLang == "Numberconian":
        for word in dictionaryz:
            if word.Numberconian == w:
                return word.translate(lang)
    elif origiLang == "Martian":
        for word in dictionaryz:
            if word.Martian == w:
                return word.translate(lang)
    elif origiLang == "Unition":
        for word in dictionaryz:
            if word.Unition == w:
                return word.translate(lang)
    elif origiLang == "Blitzion":
        for word in dictionaryz:
            if word.Blitzion == w:
                return word.translate(lang)
    elif origiLang == "Chipzion":
        for word in dictionaryz:
            if word.Chipzion == w:
                return word.translate(lang)
    else:
        for word in dictionaryz:
            if word.Morphian == w:
                return word.translate(lang)

# connect and parse msg
c = remote("prog.chal.gryphonctf.com",  17453)

while True:
    origiLang = "" # original lang
    lang = "" # language to be transalted to
    text = [] # text to be translated
    answer = ""
    try:
        reply = c.recvuntil(">", timeout=10) # recv first reply
    except Exception:
        print c.recv()
        break
    print reply
    reply = reply.splitlines()
    length = len(reply) -1
    line1 = reply[length-1].split(" ")
    line2 = reply[length].split(" ")
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
    # print "text: {}".format(text)
    for i in text:
        answer += " " + translateMe(origiLang, lang, i)
 
    print "Answer: " + answer[1:]
    c.send(answer[1:])

print c.recv()
c.close()

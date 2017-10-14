#!/usr/bin/python
import base64, hashlib
from Crypto.Cipher import AES

def AESdecrypt(ciphertext, password):
    decoded = str(base64.b64decode(ciphertext))
    decryption_suite = AES.new(password, AES.MODE_ECB)
    return decryption_suite.decrypt(decoded)

from os import listdir
from os.path import isfile, join
mypath = "/home/david/CTF/GCTF/aes/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    plaintext = ""
    key = str(f)
    fileName = "/home/david/CTF/GCTF/aes/" + f
    f = open(fileName, 'r')
    f_contents = f.read()
    ciphertext = str(f_contents.strip())
    plaintext += AESdecrypt(ciphertext, key)
    f.close()
    if "GCTF{" in plaintext:
        print plaintext
        break
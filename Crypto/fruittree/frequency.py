#!/usr/bin/python

mapping = {1:"E", 2:"T", 3:"I", 4:"A", 5:"N", 6:"R", 7:'S', 8:'O', 9:'L', 10:'M', 11:'U', 12:'C', 13:'D', 
14:'Y', 15:'F', 16:'H', 17:'G', 18:'V', 19:'W', 20:'K', 21:'B',22:'P', 23:'X', 24:'J', 25:'Q', 26:'Z', 
30:" ", 31:"_", 32:"{", 33:"}", 34:"\n"}

text = [15, 4, 10, 1, 30, 3, 7, 30, 21, 11, 2, 30, 4, 30, 15, 6, 11, 3, 2, 30, 2, 6, 1, 1, 34, 7, 8, 30, 18, 1, 6, 
14, 30, 11, 5, 7,8,11,5,13,34,3,2,30,12,4,5,30,5,1,18,1,6,30,15,9,8,6,3,7,16,34,2,3,9,30,3,2,7,30,7,2,4,9,20,30,3,7,
30,3,5,30,2,16,1,30,17,6,8,11,5,13,34,7,8,30,10,1,5,30,8,15,30,15,4,10,1,30,12,4,5,30,5,1,18,1,6,30,15,3,5,13,30,4,30,
19,4,14,34,2,3,9,9,30,2,3,10,1,30,16,4,7,30,15,9,8,19,5,34,15,4,6,30,15,6,8,10,30,2,16,1,3,6,30,13,14,3,5,17,30,13,4,14]
flag = [17, 12, 2, 15, 32, 2, 16, 3, 7, 31, 7, 8, 5, 17, 31, 3, 7, 16, 31, 2, 8, 8, 31, 7, 2, 6, 8, 5, 20, 33]
tmp = ""
plainFlag = ""
for i in flag:
    plainFlag += mapping[i]

for i in text:
    tmp += mapping[i]

print plainFlag
print tmp

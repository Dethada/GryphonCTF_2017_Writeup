#!/usr/bin/python
from PIL import Image

img = Image.open("50shadesbrighter.png")
pix = img.load()
answer = ""
numbers = []
for i in range(img.size[0]):
    numbers.append((pix[i,0][0] / 2))

for i in range(1, img.size[1]):
    numbers.append((pix[88, i][0] / 2))

for i in numbers:
    answer += chr(i)
print answer

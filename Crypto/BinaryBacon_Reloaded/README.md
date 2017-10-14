# Binary Bacon Reloaded

Didn't manage to solve this before competition ended I knew it had something to do with braille but couldn't think of how to link it together.

**Description:**

> HEllO P Eople I aM HeRE TO telL yOu SOM EThiNg i aM LEA RninG T o COmMU NicaTe WITH bl inD PEO Ple!! whA T dO yOU thINK A Bout th at? ISNT That A g oOD tHI NG? i cAn taLK TO More pe opLE AB Out mY l ove for bacon now!!!

## Solution

the flag is hidden in the cipher text in groups of 6, ignoring all spaces and punctuations 110011 100001 011011 110001 010111 110010 001111 100011 011011 100010 111100 001111 100001 101011 001111 100000 001111 100010 011011 110010 001111 100000 001111 100010

each group can be used to form braille eg,110011 would be equal to
1 1
1 1
0 0

decode and solve

flag is GCTF{wh4t_ev3n\_15_th15}
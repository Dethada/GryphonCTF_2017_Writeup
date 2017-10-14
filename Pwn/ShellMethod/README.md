# ShellMethod

## Solution

This challenge was quite a pain for me mostly because I forgot to disable ASLR but also stack is an annoying  place. Originally intended to use a return to stack exploit but changed to use return to heap due to the volatility of the stack.

Since there is no win function for this challenge we need to use shellcode. I used some shellcode I got from shellstorm.

First we need to find the address where our input is being stored to in the heap. The we point eip to that address unlike return2stack we need to put our payload before our padding.

Flag is GCTF{5h3llc0d35\_4r3\_ju57_4553mbly}
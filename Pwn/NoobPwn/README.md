# Noobpwn

## Solution

This challenge took me longer than it should've.

To solve this challenge you need to know about file descriptors https://www.bottomupcs.com/file_descriptors.xhtml

We need fd to be equals to 0 so that it reads from stdin aka our keyboard. So when prompted for the key enter 201527 (0x31337 in decimal) and then enter GIMMEDAFLAG.

Flag is GCTF{f1l3\_d35cr1p70r5\_4r3_n457y}
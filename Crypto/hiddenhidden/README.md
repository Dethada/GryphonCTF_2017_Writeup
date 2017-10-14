# Hidden Hidden

## Solution

The description says it is an simple encryption left on a loop, so first we have to find out what one loop of it does.

After some decoding we realize the data is binary > base64 > binary > base64 ... so we can assume one loop is binary to base64 back to binary now we just need to repeat the loop until the flag comes out.

flag is GCTF{100p1n65_5_4ev44a44rz}
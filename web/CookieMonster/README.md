# Cookie Monster

## Solution

Use xss to steal cookie from cookie monster.

Enter `' onerror=document.write(document.cookie) '` to the netcat service to steal the cookie monster's cookie then use that cookie value as your own and go to the cookie monster only page to get the flag.

flag is GCTF{c\_15\_f0r_c00k13\_4nd_c00k13\_15_f0r_m3}
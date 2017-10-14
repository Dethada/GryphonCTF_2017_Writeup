# Time to Crypt

## Solution

> c1 = ciphertext 1, c2 = ciphertext 2
>
> m1 = message 1, m2 = message 2
>
> c1 ^ c2 = m1 ^ m2
>
> m1 ^ m2 ^ m2 = m1

since we know m2 we can get m1 which is the flag by xoring both cipher text and m2 together.

flag is GCTF{p4ds_u53d\_0n3\_700\_m4ny_71m35}
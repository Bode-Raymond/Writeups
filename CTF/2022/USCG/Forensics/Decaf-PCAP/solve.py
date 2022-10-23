from pwn import *
import sys

binary = args.BIN
context.terminal = ['tmux', 'splitw', "-h"]
e = context.binary = ELF(binary)
r = ROP(e)

gdb_script = '''
continue
'''

def start():
    if args.GDB:
        return gdb.debug(e.path, gdbscript=gdb_script)
    elif args.REMOTE:
        return remote('0.cloud.chals.io', '22354')
    elif args.LOCAL:
        return process(e.path, level="error")

p = start()



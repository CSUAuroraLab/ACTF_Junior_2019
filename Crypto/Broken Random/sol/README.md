直接的攻击点在于[srand(time(NULL))](https://github.com/CSUwangj/ACTF_Junior_2019/blob/master/Crypto/Broken%20Random/src/src.c#L14)

srand()的效果是给rand()设置种子，问题就在于用[time(NULL)](https://linux.die.net/man/2/time)。

从文档里可以知道，time(NULL)返回从1970-01-01 00:00:00 +0000 (UTC)开始到现在的**秒**数。

所以至少有以下几种攻击方式：

1. 同时开两个terminal，同时nc一下就很有可能让两个程序用同一个种子，只需要读一个写一个就行。
2. 把程序自己编译一遍，一边nc一边运行。
3. 暴力猜一下服务器的时间。（本地暴力）。
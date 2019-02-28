这个题是HGAME2018里看到的，感觉很有意思，YTB上有更详细的视频。

[**源码**](https://github.com/CSUAuroraLab/ACTF_Junior_2019/blob/master/Linux%26PWN/Special_Shell/src/src.c)

有两个预期解，一方面来说，假如去阅读system()的[手册](https://linux.die.net/man/3/system)会看到

> Do not use **system**() from a program with set-user-ID or set-group-ID privileges, because strange values for some environment variables might be used to subvert system integrity. Use the ***exec**(3)* family of functions instead, but not ***execlp**(3)* or ***execvp**(3)*.

如果去找一些可能的实现可能可以看到下面这样的

```c
int system(const char *command)
{
    /* balabala */
        execl("/bin/sh", "sh", "-c", command, (char *) NULL);
        _exit(127);                     /* We could not exec the shell */

    /* balabala */
    return status;
}
```

所以用`$0`是可以getshell的。

另一方面来说，`man bash`一下，了解一下`meta character in bash`，可以用`/???/?? .`得出目录，然后`/???/??? ????`看到flag。
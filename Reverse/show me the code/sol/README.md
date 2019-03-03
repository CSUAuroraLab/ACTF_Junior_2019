# show me the code

我们只看比较关键的给出的代码：

```c
for (int i = 1; keystr[i]; i++) {
		keystr[i] ^= keystr[i-1];
		keystr[i] += 2;
	}
...
if(!strcmp(keystr,enstr)){
    ...
}
else{
    ...
}
```

用户的输入在经过for循环的操作之后与enstr字符串比对，若相同则提示输入正确，所以我们要做的就是从给出的enstr字符串和for循环里的操作来__逆推__出正确的输入应该是怎样的。

for循环里从第1位字符开始每个字符异或上一位的字符之后加2，加的逆操作是减，而异或的逆操作则是再次异或相同的数，比如说(a^b)^b = a ，所以我们的逆操作应该是从enstr最后一位字符开始，每一位先减2再异或前一位，循环至第1位，代码如下：

```c
#include<stdio.h>

int main(){
    char enstr[]={0x41,0x04,0x52,0x16,0x6f,0x3a,0x10,0x23,0x42,0x74,0x1b,0x31,0x70,0x49,0x7b,0x26,0x56,0x64,0x3d,0x4c,0x7e,0x0e,0x41,0x27,0x08,0x77};
    for(int j=25;j>=1;j--){
		enstr[j] -= 2;
		enstr[j] ^= enstr[j-1];
	}
	printf("%s",enstr);
    return 0;
}
```

得到flag：__ACTF{W41c0m4_70_r4_w0r1d!}__
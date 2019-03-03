# 关于我F5以后还是搞不懂他在想些什么这档事

把文件放入ida分析，进入``main`` 函数以后F5查看c代码。在接收用户输入以后有很长的一段代码：

```c
  v3 = malloc(0x82uLL);
  v14 = v3;
  v4 = qword_55FA3685F068;
  *(_QWORD *)v3 = func_s;
  *((_QWORD *)v3 + 1) = v4;
  v5 = qword_55FA3685F078;
  *((_QWORD *)v3 + 2) = qword_55FA3685F070;
  *((_QWORD *)v3 + 3) = v5;
  v6 = qword_55FA3685F088;
  *((_QWORD *)v3 + 4) = qword_55FA3685F080;
  *((_QWORD *)v3 + 5) = v6;
  v7 = qword_55FA3685F098;
  *((_QWORD *)v3 + 6) = qword_55FA3685F090;
  *((_QWORD *)v3 + 7) = v7;
  v8 = qword_55FA3685F0A8;
  *((_QWORD *)v3 + 8) = qword_55FA3685F0A0;
  *((_QWORD *)v3 + 9) = v8;
  v9 = qword_55FA3685F0B8;
  *((_QWORD *)v3 + 10) = qword_55FA3685F0B0;
  *((_QWORD *)v3 + 11) = v9;
  v10 = qword_55FA3685F0C8;
  *((_QWORD *)v3 + 12) = qword_55FA3685F0C0;
  *((_QWORD *)v3 + 13) = v10;
  v11 = qword_55FA3685F0D8;
  *((_QWORD *)v3 + 14) = qword_55FA3685F0D0;
  *((_QWORD *)v3 + 15) = v11;
  *((_WORD *)v3 + 64) = word_55FA3685F0E0;
```

这一段其实耐心看完不难发现，完成的其实只是将以``func_s``为首地址的之后130个字节的数据拷贝到以``v3``为首地址的空间里，相当于``memcpy((char *)v3,func_s,130);``。之后的内容则是将这段数据从``v3``开始，每个字节都异或``0x23``:

```c
  v17 = v14;
  v16 = 0;
  while ( v16 <= 129 )
  {
    *v17 ^= 0x23u;
    ++v16;
    ++v17;
  }
```

完成这一步后出现了一个不太寻常的操作：``((void (__fastcall *)(char *, char *))v14)(v13, v13);`` 将这一段数据当作了函数并且传入参数``v13``调用了它。最后就到了验证flag的环节。flag当然不会原模原样的放在验证数组里（经过两次挨打的出题人终于不再图样了），所以我们还是要搞清楚这段数据被当作函数调用以后对用户的输入做了什么操作。

问题来了，该怎么分析这段数据呢？一个比较省力的办法是使用ida的动态调试功能（因为是elf文件所以需要在linux的虚拟机里进行远程调试，具体的操作方法搜一蛤就能找到），在调用这段数据时下断点，程序自己运行到断点处时，单步进入，创建函数后再使用F5功能，就能看到这段数据被当作函数时是怎样的代码。经由上述操作，我们进入了获得了这段函数的代码：

```c
__int64 __fastcall sub_56389A4F1830(__int64 a1)
{
  int i; // [rsp+14h] [rbp-4h]

  for ( i = 0; *(_BYTE *)(i + a1); ++i )
    *(_BYTE *)(i + a1) = (*(unsigned __int8 *)(i + a1) << 32) & ((signed int)*(unsigned __int8 *)(i + a1) >> 32) ^ 0xCC;
  return 0LL;
}
```

a1为用户输入，经历for循环中的移位、和、异或系列操作后返回。之后就是验证环节。运算操作没有很复杂，以下是解密代码：

```c
#include<stdio.h>

int main() {
	char str[]={0x8d,0x8f,0x98,0x8a,0xb7,0xbf,0xa3,0xa0,0xba,0xa9,0x93,0xbb,0xa5,0xb8,0xa4,0x93,0xa8,0xb5,0xa2,
	0xad,0xa1,0xa5,0xaf,0x93,0xa8,0xa9,0xae,0xb9,0xab,0xab,0xa5,0xa2,0xab,0xb1};
	for(int i=0;i<=33;i++){
		for(char input = 0x20;input<=0x7e;input++){
			char input_m;
			input_m = ((input<<32)&(input>>32)^0xcc);
			if(input_m == str[i]){
				printf("%c",input);
				break;
			}
		}
	}
	return 0;
  
}
```

得到flag：__ACTF{solve_with_dynamic_debugging}__
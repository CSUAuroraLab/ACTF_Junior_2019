# simple asm

根据给出的c代码我们可以知道这整个程序的流程很简单，要求输入flag后，把输入传入func函数，以func函数的返回值判断用户输入的是否为正确的flag，所以现在要做的就是分析func函数的功能从而解出flag。接下来开始一步步分析给出的func函数的汇编码：

最开始的这一段分析需要掌握栈帧以及函数调用约定的相关知识，这里直接给出分析的结果：

```assembly
   0x0006fa <+0>:	push   rbp
   0x0006fb <+1>:	mov    rbp,rsp
   0x0006fe <+4>:	mov    QWORD PTR [rbp-0x18],rdi
   0x000702 <+8>:	mov    DWORD PTR [rbp-0x4],0x0
```

在simple.c中我们知道有这样一个调用：``func(input)`` ，而上面的汇编代码实现的是将参数``input``的地址保存到``[rbp-0x18]``这个地方。之后``[rbp-0x4]``则作为一个局部变量，为其赋值为``0x0``。到这里我们可以尝试还原一下c代码：

```c
int func(char *input){
    int i=0x0;
    ...
}
```

我们将``[rbp-0x4]``假设为int型变量i，``[rbp-0x18]``假设为指向用户输入字符串首地址的指针input，往后看:

```assembly
 0x000709 <+15>:	jmp    0x75d <func+99>
 ...
 0x00075d <+99>:	cmp    DWORD PTR [rbp-0x4],0x15
 0x000761 <+103>:	jle    0x70b <func+17>
```

跳转到<func+99>后将``[rbp-0x4]``中的值（也就是i）与``0x15``比较，只要不大于``0x15``就会跳转到<func+17>处。因为i的初值为``0x0``，所以会实现跳转。

```assembly
 0x00070b <+17>:	mov    eax,DWORD PTR [rbp-0x4]
 0x00070e <+20>:	movsxd rdx,eax
 0x000711 <+23>:	mov    rax,QWORD PTR [rbp-0x18]
 0x000715 <+27>:	add    rax,rdx
 0x000718 <+30>:	movzx  edx,BYTE PTR [rax]
```

根据先前的假设，前四行相当于完成了``(input+i)``,使input指向第i位字符；再看最后的``movzx  edx,BYTE PTR [rax]``,这里实现了寻址到``(input+i)``所表示的地址处并将此地址内存储的值传给edx，写成伪c代码相当于``edx = *(input + i)`` 。

```assembly
 0x00071b <+33>:	mov    eax,DWORD PTR [rbp-0x4]
 0x00071e <+36>:	movsxd rcx,eax
 0x000721 <+39>:	mov    rax,QWORD PTR [rbp-0x18]
 0x000725 <+43>:	add    rax,rcx
 0x000728 <+46>:	add    edx,0x7
 0x00072b <+49>:	mov    BYTE PTR [rax],dl
```

这里是比较关键的一个点，前四行进行的是与上一段相同的工作，到了第五行出现了使``edx``的值加7的操作，而在之前的分析中此时``edx``中存放的是``*(input+i)``，最后一行则是将加7之后的结果赋给原``(input+i)``的地址处。综上，上面的两段汇编实现了:  `` *(input+i) += 7``，继续往下看：

```assembly
   0x00072d <+51>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000730 <+54>:	movsxd rdx,eax
   0x000733 <+57>:	mov    rax,QWORD PTR [rbp-0x18]
   0x000737 <+61>:	add    rax,rdx
   0x00073a <+64>:	movzx  ecx,BYTE PTR [rax]
   0x00073d <+67>:	mov    eax,DWORD PTR [rbp-0x4]
   0x000740 <+70>:	movsxd rdx,eax
   0x000743 <+73>:	lea    rax,[rip+0x2008f6]        # 0x201040 <enstr>
   0x00074a <+80>:	movzx  eax,BYTE PTR [rdx+rax*1]
```

前5行做的是一样的事，写成伪代码就是 ``ecx = *(input + i)`` ; 之后2行则为``rdx = i``; 最后2行比较关键，`` lea    rax,[rip+0x2008f6] ``所做的是将simple.c中给出的字符数组``enstr``的首地址存入``rax``，而后综合前面的分析可以得出伪代码`` eax = *(enstr + i)``，之后是比较和跳转操作：

```assembly
   0x00074e <+84>:	cmp    cl,al
   0x000750 <+86>:	je     0x759 <func+95>
   0x000752 <+88>:	mov    eax,0x1
   0x000757 <+93>:	jmp    0x768 <func+110>
   0x000759 <+95>:	add    DWORD PTR [rbp-0x4],0x1
   0x00075d <+99>:	cmp    DWORD PTR [rbp-0x4],0x15
   0x000761 <+103>:	jle    0x70b <func+17>
   0x000763 <+105>:	mov    eax,0x0
   0x000768 <+110>:	pop    rbp
   0x000769 <+111>:	ret
```

由之前的分析可以很容易看懂这里第一行的``cmp``操作:``*(input + i)``与``*(enstr + i)``比对（此时``*(input + i)``已经经过了加7的操作），相等则跳转到<func+95>继续执行，i的值加1，又进入<func+99>处的判断（可知这里应该是个while循环），直到i的值大于0x15后，给``eax``赋0，即此函数的返回值将为0，退回栈帧后返回；不相等则给``eax``赋1，即此函数的返回值将为1，跳转到<func+110>退回栈帧后返回。综合所有分析，完成c代码的还原:

```c
int func(unsigned char *input){
	for(int i=0;i<=21;i++){
		input[i]+=7;
		if(input[i]!=enstr[i]){
			return 1;
		}
	}
	return 0;
}
```

我们只要将给出的``enstr``所有值减7，就能拿到flag：

__ACTF{a5m_15_1mp0r7an7} __


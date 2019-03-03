考核：
写脚本发送POST请求

解题代码：

```python
import requests

r  = requests.session()

data={
    'just':'have fun',
}

for i in range(6666):
    s = r.post('http://149.129.66.40:29016/index.php',data=data).text
    print(i)
    if 'ACTF' in s:
        print(s[-80:])


```


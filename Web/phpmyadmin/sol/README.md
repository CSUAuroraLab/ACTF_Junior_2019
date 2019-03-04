考核： CVE-2018-12613

环境来自P神的靶场：

https://github.com/vulhub/vulhub/blob/master/phpmyadmin/CVE-2018-12613/README.zh-cn.md
解题：

![](https://i.imgur.com/82dm7PY.png)
CVE-2018-12613的正常操作是包含session文件然后执行命令

有同学使用frm文件不成功是因为靶场使用了两个docker，mysql和phpmyadmin分开来了，所以把frm文件写入到mysql docker里，但是我们能访问的是phpmyadmin的docker，而phpmyadmin docker没有frm文件。

还有一种方法就是直接在`/var/www/html`目录直接写shell
考核：ssh连接服务器，linux文件读取
环境搭建：

```
# 启动docker
docker run -d \
  --name ssh.1 \
  -p 2020:22 \
  --env "SSH_USER=aurora" \
  --env "SSH_PASSWORD_AUTHENTICATION=true" \
  jdeathe/centos-ssh:centos-7

# 删除docker
docker stop ssh.1 \
  && docker rm ssh.1 \
```

解题：
SSH登录之后，cat flag即可
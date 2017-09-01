import requests
import urllib.request
from lxml import etree
import random
import re
import os
import time
from urllib.error import URLError
import socket


n = random.randint(0,5)
f = open("test.txt","r")
lines = f.readlines()#读取全部内容
for line in lines:

    url = line
    keep_request = True
    while keep_request:
        try:
            html = urllib.request.urlopen(url,timeout=5).read()
            keep_request = False
        except URLError:
            # 遇到错误，等待
            print("主页error")
            time.sleep(1)
        except socket.timeout:
            # 遇到错误，等待
            print("主页error socket")
            time.sleep(1)
        except ConnectionResetError:
            print("主页10054 error")
            time.sleep(5)
    print("正在下载", url)
    selector = etree.HTML(html)
    page = selector.xpath('//div[@class="page"]//a//@href')
    pages = list(set(page))
    lists = ['http://www.xgyw.cc' + x for x in pages]
    for l in lists:
        keep_request = True
        while keep_request:
            try:
                ml = urllib.request.urlopen(l, timeout=5).read()
                keep_request = False
            except URLError:
                # 遇到错误，等待
                print("分页error")
                time.sleep(1)
            except socket.timeout:
                # 遇到错误，等待
                print("分页error socket")
                time.sleep(1)
            except ConnectionResetError:
                print("分页10054 error")
                time.sleep(5)
        selector = etree.HTML(ml)
        content = selector.xpath('//div[@class="img"]//img//@src')
        contents = ['http://www.xgyw.cc' + x for x in content]
        for c in contents:
            name = c[-12:]
            os.chdir(r"E:\test\rosi1")
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            }
            request = urllib.request.Request(c,None,header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
            keep_request = True
            while keep_request:
                try:
                    # 你的代码
                    response = urllib.request.urlopen(request,timeout=5).read()
                    print(c)
                    keep_request = False

                except URLError:
                    # 遇到错误，等待
                    print("error")
                    time.sleep(1)
                except socket.timeout:
                    # 遇到错误，等待
                    print("error socket")
                    time.sleep(1)
                except ConnectionResetError:
                    print("10054 error")
                    time.sleep(5)

            f = open(name, 'wb')
            f.write(response)
            f.close()
            print(name)
            time.sleep(n)
            # socket.setdefaulttimeout(5.0)
            # urllib.request.urlretrieve(c, r'E:\test\rosi1\%s' % name)
    print("下载完成")
    print('\n')
        # os.chdir(r"F:\test\rosi")
        # header = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        # }
        # request = urllib.request.Request(c,None,header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
        # response = urllib.request.urlopen(request)
        # f = open(name, 'wb')
        # f.write(response.read())
        # f.close()
        # print(c)
# lists = ['http:' + x for x in content]
    # y = 1
    # for l in lists:
    #     urllib.request.urlretrieve(l, r'F:\test\image\%s_%d.jpg' % (z, y))
    #     print('%s_%d正在保存' % (z, y))
    #     y += 1
    # z-=1

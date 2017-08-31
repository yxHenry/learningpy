import requests
import urllib.request
from lxml import etree
import random
import re
import os
import time

url = "http://www.xgyw.cc/Rosimeimei/Rosimeimei7033.html"
try:
    html = urllib.request.urlopen(url, timeout=5)
    response = html.read()
except Exception as e:
    print(e)
selector = etree.HTML(response)
pages = selector.xpath('//div[@class="page"]//a//@href')
lists = ['http://www.xgyw.cc' + x for x in pages]
for l in lists:
    try:
        html = urllib.request.urlopen(l,timeout=5)
        response = html.read()
    except Exception as e:
        print(e)
    selector = etree.HTML(response)
    content = selector.xpath('//div[@class="img"]//img//@src')
    contents = ['http://img.xgyw.cc' + x for x in content]
    for c in contents:
        name = c[-12:]
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(c, r'F:\test\rosi\%s' % name)
        print(c)
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

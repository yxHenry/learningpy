import requests
import urllib.request
from lxml import etree
import random
import re
import os
import time

# proxy = {'http': '27.24.158.155:84'}
# proxy_support = urllib.request.ProxyHandler(proxy)
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
#
# import urllib2
# import random
#
#
# def getHtml(url, proxies):
#     random_proxy = random.choice(proxies)
#     proxy_support = urllib2.ProxyHandler({"http": random_proxy})
#     opener = urllib2.build_opener(proxy_support)
#     urllib2.install_opener(opener)
#     html = urllib2.urlopen(url)
#     return html
#
#
# url = "http://www.csdn.net/"
# proxies = ["101.53.101.172:9999", "171.117.93.229:8118", "119.251.60.37:21387", "58.246.194.70:8080"
#                                                                                 "115.173.218.224:9797",
#            "110.77.0.70:80"]
# for i in range(0, 10000):
#     try:
#         html = getHtml(url, proxies)
#         print
#         html.info()  # 打印网页的头部信息，只是为了展示访问到了网页，可以自己修改成想显示的内容
#         print
#         i
#     except:
#         print
#         "出现故障"

url = "http://www.xgyw.cc/Rosimeimei/Rosimeimei7033.html"
try:
    html = urllib.request.urlopen(url, timeout=5)
    response = html.read()
except:
    html = urllib.request.urlopen(url, timeout=5)
    response = html.read()
selector = etree.HTML(response)
pages = selector.xpath('//div[@class="page"]//a//@href')
lists = ['http://www.xgyw.cc' + x for x in pages]
for l in lists:
    try:
        html = urllib.request.urlopen(l,timeout=5)
        response = html.read()
    except:
        html = urllib.request.urlopen(l, timeout=5)
        response = html.read()
    selector = etree.HTML(response)
    content = selector.xpath('//div[@class="img"]//img//@src')
    contents = ['http://img.xgyw.cc' + x for x in content]
    for c in contents:
        name = c[-12:]
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(c, r'E:\test\rosi\%s' % name)
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

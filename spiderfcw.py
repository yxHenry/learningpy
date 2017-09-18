import urllib.request
import re
import time
import requests
import os
from bs4 import BeautifulSoup

import random

url = 'http://www.fcw30.com/sitemap.xml?type=videos&from_links_videos=1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
response = requests.get(url,headers=headers)
req = response.text
# response = urllib.request.urlopen(url)
# html = response.read().decode('utf-8')
# print(req)
res_tr = r'<video:content_loc>(.*?)</video:content_loc>'
m_tr = re.findall(res_tr,req)
for mm in m_tr:
    print(mm)
    name=mm[-10:-5]
    print(name)
    if os.path.exists(r'E:\test\%s.mp4' % name):
        pass
    else:
        urllib.request.urlretrieve(mm, r'E:\test\%s.mp4' % name)
        print(name,"下载完成")


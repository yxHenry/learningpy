import re
import urllib
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html


def getImg(html):
    reg=r'src="(.+?\.jpg)" size='
    imgre=re.compile(reg)
    html = html.decode('utf-8')
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg'%x)    #urllib.urlretrieve()方法，直接将远程数据下载到本地。
        x+=1


name='http://tieba.baidu.com/p/4859088308'
html=getHtml(name)
getImg(html)
print('DONE!')
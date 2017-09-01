import urllib.request
from lxml import etree


i = int(input("需要爬取的页数："))
for num in range(1,i+1):
    if num ==1:
        url = "http://www.xgyw.cc/Rosimeimei"
        html = urllib.request.urlopen(url)
        response = html.read()
        selector = etree.HTML(response)
        pages = selector.xpath('//div[@class="nr"]//td[@class="td6"]//a//@href')
        r_pages = ["http://www.xgyw.cc"+ x for x in pages]

    else:
        url = "http://www.xgyw.cc/Rosimeimei/page_" + str(num) + ".html"
        html = urllib.request.urlopen(url)
        response = html.read()
        selector = etree.HTML(response)
        pages = selector.xpath('//div[@class="nr"]//td[@class="td6"]//a//@href')
        r_pages = ["http://www.xgyw.cc" + x for x in pages]
    page_sort = sorted(r_pages)
    for r in page_sort:
        f = open('test.txt', 'a')
        f.write(r)
        f.write("\n")
        f.close()
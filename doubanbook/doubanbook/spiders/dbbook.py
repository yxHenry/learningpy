# -*- coding: utf-8 -*-
import scrapy


class DbbookSpider(scrapy.Spider):
    name = 'dbbook'
    #allowed_domains = ['www.douban.com/doulist/1264675/']
    start_urls = ['http://www.douban.com/doulist/1264675/']

    def parse(self, response):
        print(response.body)

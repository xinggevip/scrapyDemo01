# -*- coding: utf-8 -*-
import scrapy
import json

class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print('来到了解析')
        ip = json.loads(response.text)
        print(ip)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)
        pass

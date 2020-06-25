# -*- coding: utf-8 -*-
import scrapy


class MyselfblogSpider(scrapy.Spider):
    name = 'myblog'
    allowed_domains = ['qiangssvip.com']
    start_urls = ['http://qiangssvip.com/']

    def parse(self, response):
        print('-' * 40)
        print(response)
        print(type(response))
        print('-' * 40)
        pass

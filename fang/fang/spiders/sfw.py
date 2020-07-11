# -*- coding: utf-8 -*-
import scrapy
import json

class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        # 获取所有tr标签
        trs = response.xpath('//table[@class="table01"]//tr')
        for tr in trs:
            print("="*30)
            print(tr)

        pass

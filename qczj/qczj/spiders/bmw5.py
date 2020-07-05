# -*- coding: utf-8 -*-
import scrapy
from qczj.items import QczjItem


class Bmw5Spider(scrapy.Spider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438/']

    def parse(self, response):
        print('*' * 30)
        print(response)
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in  uiboxs:
            category = uibox.xpath('./div[@class="uibox-title"]/a/text()').get()
            # print(category)
            urls = uibox.xpath('./div/ul/li/a/img/@src').getall()
            '''
            for url in urls:
                # print('https:' + url)
                print(response.urljoin(url))
            print('*' * 50)
            '''
            urls = list(map(lambda url:response.urljoin(url),urls))
            item = QczjItem(category = category,urls = urls)
            # print(urls)
            # print('*' * 50)
            yield item


        pass

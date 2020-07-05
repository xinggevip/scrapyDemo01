# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qczjpro.items import QczjproItem

class BmoimgSpider(CrawlSpider):
    name = 'BmoImg'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65-\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/photo/series/.*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        category = response.xpath('//div[@id="outlink"]/a[1]//text()').get()
        image_urls = [response.urljoin(response.xpath('//img[@id="img"]/@src').get())]
        item = QczjproItem(category = category,image_urls = image_urls)

        yield item

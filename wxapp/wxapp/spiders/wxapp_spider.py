# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+portal\.php\?mod=list&catid=\d&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r".+article-.*\.html"),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        title = response.xpath("//h1[@class='ph']/text()").get()
        author = response.xpath("//p[@class='authors']/a/text()").get()
        push_time = response.xpath("//p[@class='authors']/span/text()").get()
        content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(content).strip()
        item = WxappItem(title=title,author=author,push_time=push_time,content=content)
        return item

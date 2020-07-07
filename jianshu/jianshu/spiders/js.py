# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        '''
            scrapy shell url
            title = scrapy.Field()
            avatar = scrapy.Field()
            author = scrapy.Field()
            pub_time = scrapy.Field()
            article_id = scrapy.Field()
        '''
        title = response.xpath('//h1[@class="_1RuRku"]/text()').get()
        avatar = response.xpath('//meta[@property="og:image"]/@content').get()
        author = response.xpath('//span[@class="_22gUMi"]/text()').get()

        pub_time = response.body.re(r'last_updated_at":(.*?),')
        print(title)
        yield title
        pass

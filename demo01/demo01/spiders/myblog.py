# -*- coding: utf-8 -*-
import scrapy
from demo01.items import Demo01Item


class MyblogSpider(scrapy.Spider):
    name = 'myblog'
    allowed_domains = ['qiangssvip.com']
    start_urls = ['http://qiangssvip.com/']

    def parse(self, response):
        print('-' * 40)
        # <class 'scrapy.http.response.html.HtmlResponse'>
        print(response)
        # <class 'scrapy.selector.unified.SelectorList'>
        contentList = response.xpath('//div[@class="post-meta wrapper-lg"]')

        for content in contentList:
            # 获取标题
            h2 = content.xpath(".//h2/a/text()").get()
            print(h2)
            # 获取内容
            summary = content.xpath(".//p/text()").getall()
            summary = "".join(summary).strip()
            print(summary)

            # 存储数据
            # article = {"title":h2,"content":summary}
            # yield article

            item = Demo01Item(title=h2,content=summary)
            yield item
            pass
        next_url = response.xpath("//ol/li[@class='next']/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(next_url,callback=self.parse)
        print('-' * 40)
        pass

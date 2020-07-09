# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu.items import ArticleItem
import time

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

        # TODO 用正则取有问题，暂时不取了
        # pub_time = response.body.re(r'last_updated_at":(.*?),')

        url = response.url
        urlArr = url.split('?')
        urlRes = urlArr[0]
        article_id = urlRes.split('/')[-1]
        content = ''.join(response.xpath('//article[@class="_2rhmJa"]//text()').getall())


        now = int(round(time.time() * 1000))
        pub_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))

        try:
            like_count = int(response.xpath('//span[@class="_1GPnWJ"]/text()').get())
            commit_count = int(response.xpath('//div[@class="_3nj4GN"]//span[1]/text()[2]').get())
            word_count = int(response.xpath('//div[@class="s-dsoj"]//span[2]/text()').get().replace(' ','').replace(',','').replace('字数',''))
            subjects = ','.join(response.xpath('//span[@class="_2-Djqu"]//text()').getall())
            read_count = int(response.xpath('//div[@class="s-dsoj"]//span[3]/text()').get().replace(' ','').replace(',','').replace('阅读','')
)

            item = ArticleItem(
                title = title,
                avatar = avatar,
                author = author,
                pub_time = pub_time,
                article_id = article_id,
                origin_url = url,
                content = content,
                like_count = like_count,
                commit_count = commit_count,
                word_count = word_count,
                subjects = subjects,
                read_count = read_count

            )
            yield item
        except:
            print('捕获到异常' + '*' * 30)

            item = ArticleItem(
                title=title,
                avatar=avatar,
                author=author,
                pub_time=pub_time,
                article_id=article_id,
                origin_url=url,
                content=content
            )
            yield item

            pass
        pass

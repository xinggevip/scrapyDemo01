# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    avatar = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    article_id = scrapy.Field()
    origin_url = scrapy.Field()
    content = scrapy.Field()
    read_count = scrapy.Field()
    like_count = scrapy.Field()
    word_count = scrapy.Field()
    subjects = scrapy.Field()
    commit_count = scrapy.Field()
    pass

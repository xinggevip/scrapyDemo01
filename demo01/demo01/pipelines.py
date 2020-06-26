# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
import json

class Demo01Pipeline:
    def __init__(self):
        self.file = open('article.json', 'w',encoding='utf-8')

    def open_spider(self,spider):
        print("爬虫开始...")
        pass

    def process_item(self, item, spider):
        print("存储")
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(item_json + '\n')
        return item

    def close_spider(self,spider):
        print("爬虫结束")
        self.file.close()
        pass
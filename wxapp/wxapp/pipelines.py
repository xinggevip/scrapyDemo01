# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
class WxappPipeline:
    def __init__(self):
        self.file = open('wxapp.json','wb')
        self.export = JsonLinesItemExporter(self.file,ensure_ascii=False,encoding='utf-8')
        pass

    def open_spider(self, spider):
        print("爬虫开始...")
        pass

    def process_item(self, item, spider):
        print("存储...")
        self.export.export_item(item)
        return item
        pass

    def close_spider(self, spider):
        print("爬虫结束...")
        self.file.close()
        pass
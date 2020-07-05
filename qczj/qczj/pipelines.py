# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request

class QczjPipeline:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

        if not os.path.exists(self.path):
            os.mkdir(self.path)

        pass


    def process_item(self, item, spider):
        # 判断category文件夹是否存在,不存在则创建分类文件夹
        categoryPath = os.path.join(self.path,item['category'])
        if not os.path.exists(categoryPath):
            os.mkdir(categoryPath)

        for index, url in enumerate(item['urls']):
            # image_name = item['category'] + '_' + str(index) + '.jpg'
            image_name = url.split('_')[-1]
            request.urlretrieve(url, os.path.join(categoryPath,image_name))
            pass


        return item

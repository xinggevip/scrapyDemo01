# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from qczjpro import settings

class QczjproPipeline:
    def process_item(self, item, spider):
        return item

class QczjBmwImagesPipelines(ImagesPipeline):

    # 发送请求之前调用
    def get_media_requests(self, item, info):
        request_objs = super(QczjBmwImagesPipelines, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
            pass

        return request_objs
        pass


    def file_path(self, request, response=None, info=None):
        # TODO 如果项目目录下的images文件夹不存在则创建，想在init中创建但是 一重写就报错
        images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(images_path):
            os.mkdir(images_path)

        # 图片在存储之前调用，用来获取图片的存储路径
        path = super(QczjBmwImagesPipelines, self).file_path(request,response,info)  # full/文件名.jpg
        category = request.item.get('category') # 车身外观
        images_store = settings.IMAGES_STORE # 项目路径/images/
        category_path = os.path.join(images_store,category) # 项目路径/images/车身外观/
        if not os.path.exists(category_path):
            os.mkdir(category_path)
            pass

        info = request.item.get('info')
        info_path = os.path.join(category_path, info)
        if not os.path.exists(info_path):
            os.mkdir(info_path)
            pass


        image_name = path.replace('full/', '')  # 68529e411d7e144877e49fa5a28e769986ddf027.jpg 哈希文件名
        # image_name = request.item.get('category') + path.replace('full/','') # 重要特点68529e411d7e144877e49fa5a28e769986ddf027.jpg 分类名称哈希文件名
        image_path = os.path.join(info_path,image_name) # 项目路径/images/车身外观/文件名.jpg
        return image_path
        pass

    # 类结束
    pass
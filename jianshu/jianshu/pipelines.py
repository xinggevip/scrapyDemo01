# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi

class JianshuPipeline:
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'database': 'jianshu',
            'charset': 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
        pass

    def process_item(self, item, spider):
        # print(item)
        self.cursor.execute(self.sql, (item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = 'insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values (null,%s,%s,%s,%s,%s,%s,%s)'
            return self._sql
        return self._sql

class JianshuTwistedPipline(object):

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'database': 'jianshu',
            'charset': 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self._sql = None

    def process_item(self, item, spider):
        # 异步执行执行sql语句
        defer = self.dbpool.runInteraction(self.insert_item, item)
        # 异常处理
        defer.addErrback(self.handle_error, item, spider)
        return item

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (
        item['title'], item['content'], item['author'], item['avatar'], item['pub_time'], item['origin_url'],
        item['article_id']))
        pass

    def handle_error(self, error, item, spider):
        print('=' * 10 + 'error' + '=' * 10)
        print(error)
        print('=' * 10 + 'error' + '=' * 10)
        pass


    @property
    def sql(self):
        if not self._sql:
            self._sql = 'insert into article(id,title,content,author,avatar,pub_time,origin_url,article_id) values (null,%s,%s,%s,%s,%s,%s,%s)'
            return self._sql
        return self._sql


#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/6 9:51 
# @Author : gaoxing 
# @Version：V 0.1
# @File : start.py

from scrapy import cmdline

# cmdline.execute('scrapy crawl httpbin'.split())
cmdline.execute('scrapy crawl ipproxy'.split())
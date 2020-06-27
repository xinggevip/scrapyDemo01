#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/26 22:00
# @Author: gaoxing
# @Email: 1511844263@qq.com
# @File: start.py

from scrapy import cmdline

cmdline.execute("scrapy crawl renren_spider".split())

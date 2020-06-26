#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/26 10:48
# @Author: gaoxing
# @Email: 1511844263@qq.com
# @File: start.py

from scrapy import cmdline

# 执行cmd命令，参数是字符串列表
# 两种写法等价
# cmdline.execute(["scrapy","crawl","myblog"])
cmdline.execute("scrapy crawl myblog".split())
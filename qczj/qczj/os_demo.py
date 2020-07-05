#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2020/7/5 15:48
# @Author: gaoxing
# @Email: 1511844263@qq.com
# @File: os_demo.py

import os

imagesPath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')

if not os.path.exists(imagesPath):
    print('%s文件夹不存在' % imagesPath)
    os.mkdir(imagesPath)
else:
    print('%s文件夹已存在' % imagesPath)
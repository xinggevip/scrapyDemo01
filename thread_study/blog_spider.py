#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2021-10-22 20:46
# @Author: gaoxing
# @Email: 1511844263@qq.com
# @File: blog_spider.py

import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(3,20 + 1)
]

print(urls)


def craw(url):
    r = requests.get(url)
    return  r.text

def parse(html):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all(attrs={'class':'post-item-title'})
    return [(link['href'],link.get_text()) for link in links]

if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)
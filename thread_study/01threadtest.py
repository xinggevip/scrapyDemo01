#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2021-10-22 20:54
# @Author: gaoxing
# @Email: 1511844263@qq.com
# @File: 01threadtest.py
import blog_spider
import threading
import time

def single_thread():
    print("single_thread start")
    for url in blog_spider.urls:
        print(url)
        html = blog_spider.craw(url)
        # res = blog_spider.parse(html)
        # print(res)
    print("single_thread end")

def multi_thread():
    print("multi_thread start")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw,args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread end")

if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("单线程爬虫耗时",end - start,"秒")

    start = time.time()
    multi_thread()
    end = time.time()
    print("多线程爬虫耗时", end - start, "秒")
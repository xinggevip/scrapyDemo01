#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2021-10-22 21:56
# @Author: gaoxing
# @Email: 1511844263@qq.com
# @File: 02producer_consumer_spider.py

import queue
import blog_spider
import time
import random
import threading

def do_craw(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(threading.current_thread().name,f"craw {url}","url_queue.size=",url_queue.qsize())
        time.sleep(random.randint(1,2))

def do_parse(html_queue:queue.Queue, fout):
    while True:
        html = html_queue.get()
        res = blog_spider.parse(html)
        for item in res:
            fout.write(str(item) + "\n")
        print(threading.current_thread().name, f"res.len {len(res)}", "html.size=", len(html),"html.queue.size",html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue= queue.Queue()

    for url in blog_spider.urls:
        url_queue.put(url)

    for i in range(3):
        t = threading.Thread(target=do_craw,args=(url_queue,html_queue),name=f"craw{i}")
        t.start()

    fout = open("02data.txt","w",encoding='utf-8')

    for i in range(3):
        t = threading.Thread(target=do_parse,args=(html_queue,fout),name=f"parser{i}")
        t.start()
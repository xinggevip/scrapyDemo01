# -*- coding: utf-8 -*-
import scrapy
import json


class JuzimiLoginSpider(scrapy.Spider):
    name = 'juzimi_login'
    allowed_domains = ['juapi.qiangssvip.com','ju.qiangssvip.com']
    start_urls = ['http://juapi.qiangssvip.com/api/login']

    def start_requests(self):
        print("登录")
        url = "http://juapi.qiangssvip.com/api/login"
        data = {"userId":"xinggevip","userPassword":"123"}
        header = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        # yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse,headers=header)
        yield scrapy.Request(url=url,body=json.dumps(data),method='POST',headers=header)
        pass
    # def parse_page(self,response):
    #     print("打印")
    #     print(response.text())
    #     pass

    def parse(self, response):
        print("来到了parse")
        print(response.text)
        with open('err.html','w',encoding='utf-8') as file:
            file.write(response.text)

        pass

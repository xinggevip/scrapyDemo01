# -*- coding: utf-8 -*-
import scrapy
import execjs

class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/959949881/profile']

    def start_requests(self):
        # 生成唯一时间戳
        with open("./src/renrenLogin.js", 'r', encoding='utf-8') as f:
            js_code = f.read()
        # print(js_code)
        res = execjs.compile(js_code).call("getUniqueTimestamp")
        print("res = %s" % res)

        url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=" + res
        data = {
            'email': '15937067033',
            'password': 'hhq1511844263',
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type': 'web_login',
            'f': '',
        }
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request
        pass

    def parse_page(self,response):
        print(response.text)
        yield scrapy.Request('http://www.renren.com/959949881/profile',callback=self.parse)
        pass

    def parse(self, response):
        print("来到了parse")
        print(response.text)
        with open('profile.html','w',encoding='utf-8') as f:
            f.write(response.text)
        pass

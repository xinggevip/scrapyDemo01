# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from PIL import Image

class WeshopSpider(scrapy.Spider):
    name = 'weshop'
    allowed_domains = ['weshop.qiangssvip.com']
    start_urls = ['http://weshop.qiangssvip.com/Admin/Public/login']

    def parse(self, response):
        url = 'http://weshop.qiangssvip.com/Admin/Public/login'
        data = {
            'username': 'admin',
            'userpass': '123456',
            'verify': ''
        }
        with open("weshopLogin.html","w",encoding='utf-8') as f:
            f.write(response.text)

        # 获取图片地址
        # 通过xpath
        # img_url = 'http://weshop.qiangssvip.com' + response.xpath("//img[@id='verifyimg']/@src").get()
        # 通过css获取
        img_url = 'http://weshop.qiangssvip.com' + response.css("img#verifyimg::attr(src)").get()
        print(img_url)
        captcha = self.regonize_captcha(img_url)
        data['verify'] = captcha
        print(data)

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_after_login)
        pass

    def parse_after_login(self,response):
        print(response.text)
        pass

    def regonize_captcha(self,img_url):
        request.urlretrieve(img_url,'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input("请输入验证码:")
        return captcha
        pass

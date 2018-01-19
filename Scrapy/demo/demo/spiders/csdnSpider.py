# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/17 17:35'

import scrapy


class CsdnPostSpider(scrapy.Spider):
    '''
    构建一个csdn爬虫操作
    '''
    # 在命令行调用的名称
    name = 'csdn'
    # 允许在哪个域名下爬取
    allowed_domains = ['csdn.net']
    # 需要爬取的url地址
    start_urls = [
        'https://passport.csdn.net/account/login?ref=toolbar'
    ]

    def parse(self, response):
        '''
        进行数据筛选
        :param response:
        :return:
        '''
        # 得到请求中需要的登录流水号
        It = response.xpath("//input[@name='lt']/@value").extract()[0]

        return scrapy.FormRequest.from_response(
            response,
            formdata = {
                'username':'18937506461',
                'password':'Gaishitaibao`',
                'It':It
            },
            callback = self.parse_response
        )

    def parse_response(self, response):
        '''
        处理post请求响应数据
        :param response:
        :return:
        '''
        with open('csdn.html', 'w') as f:
            f.write(response.body)




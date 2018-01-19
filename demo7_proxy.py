# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/9 21:40'

import urllib2

# 定义url地址和请求对象
url = 'https://www.taobao.com'
request = urllib2.Request(url)

# 构建一个可以操作代理服务器的Handler对象
proxy_handler = urllib2.HTTPHandler({'https':'121.31.100.11:8123'})

# 构建一个opener对象
proxy_opener = urllib2.build_opener(proxy_handler)

response = proxy_opener.open(request)

print(response.read())

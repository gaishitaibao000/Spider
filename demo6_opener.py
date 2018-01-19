# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/9 21:06'

# 引入需要的模块
import urllib2

# 定义访问地址
url = "https://www.taobao.com"
request = urllib2.Request(url)

# 创建一个自定义的Handler对象
http_handler = urllib2.HTTPHandler()
# 构建一个opener对象
http_opener = urllib2.build_opener(http_handler)
# 发送请求
response = http_opener.open(request)

print(response.read())

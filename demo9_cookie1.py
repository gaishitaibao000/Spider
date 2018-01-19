# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/9 21:49'

import urllib2
import cookielib

# 创建cookie核心对象
cookie = cookielib.CookieJar()

# 创建一个自定义的handler
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 创建一个可以操作cookie的opener对象
cookie_opener = urllib2.build_opener(cookie_handler)

# 发送一个请求
response = cookie_opener.open('https://www.baidu.com')

# 查看cookie中出现什么数据
for i in cookie:
    print('%s-%s'%(i.name, i.value))


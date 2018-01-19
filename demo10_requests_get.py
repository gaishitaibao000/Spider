# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/10 15:41'

import requests

# 定义get参数，是一个字典数据
get_param = {
    'wd':'火影'
}

# get参数，通过params参数赋值，直接传递
response = requests.get('http://www.baidu.com', params=get_param)

print(response.text)


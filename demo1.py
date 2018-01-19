# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/8 19:12'

import urllib2
import datetime

def spider(name, num):

    for i in range(num):
        # 页数
        page_num = i+1
        print '第%s次开始读取'%page_num
        # 每页条数
        single_page_num = i*50
        # 打开链接
        response = urllib2.urlopen('https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s'%(name, single_page_num))
        # 读取页面内容
        content = response.read()
        time_now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        new_name = name.decode('utf-8').encode('GBK')
        # 开始保存写入
        with open('%s_%s_%s.html'%(new_name, i, time_now), 'w') as f:
            print '开始写入，开始爬取时间：%s'%time_now
            f.write(content)
            print '写入结束，结束爬取时间：%s'%time_now


if __name__ == '__main__':
    spider('pyhon爬虫', 8)


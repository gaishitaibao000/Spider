# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/9 17:50'

import urllib2
import time
start_time = time.time()

# python默认ascii编码，现在写入内容不是ascii编码所以要对编码进行修改
# 详情见http://blog.csdn.net/thesnowboy_2/article/details/51778653
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 获取爬取信息
kw = raw_input('请输入想要爬取的电影类：')
start_num = raw_input('请输入从第几个电影开始：')
num = raw_input('请输入想要爬取电影个数：')

# 创建文件夹
# import os
# os.mkdir('./%s'%kw.decode('utf-8').encode('gbk'))

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag={}&page_limit={}&page_start={}'.format(kw, num, start_num)

response = urllib2.urlopen(url)

sub = response.read() # json字符串类型
import json
data = json.loads(sub) # 转化成python对象list

a = 0
for movie in data['subjects']:
    # 获取电影名称
    a += 1
    with open('./%s/%s.txt'%(kw.decode('utf-8').encode('gbk'), str(a)), 'wb') as f:
        f.write(movie['title']+movie['rate'])

dirname = '最新'.decode('utf-8').encode('gbk')

import os
listdir = os.listdir('./{}/'.format(dirname))

print(sum(map(lambda x:os.path.getsize('./%s/'%dirname+x),[x for x in listdir])))

end_time = time.time()
print(end_time-start_time)
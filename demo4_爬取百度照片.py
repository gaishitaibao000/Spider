# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/9 15:05'

import urllib, urllib2

headers = {
    #'Host': 'image.baidu.com',
    #'Connection': 'keep-alive',
    #'Accept': 'text/plain, */*; q=0.01',
    #'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%BC%A0%E5%AD%A6%E5%8F%8B&oq=%E5%BC%A0%E5%AD%A6%E5%8F%8B&rsp=-1',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BDqhfp=%E5%BC%A0%E5%AD%A6%E5%8F%8B%26%260-10-1undefined%26%260%26%261; BAIDUID=02D2E3F686BD66B010CAC49F95B5DD19:FG=1; BIDUPSID=02D2E3F686BD66B010CAC49F95B5DD19; PSTM=1513601890; BDUSS=W52QUZvY2swYXllWXlFczh2SEktLVFlbU5rRUZxekxvNXJqeXhhbnFsbVhCV2RhQVFBQUFBJCQAAAAAAAAAAAEAAADHdRWH0~uzybTzyvdhc2QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJd4P1qXeD9aU; H_PS_PSSID=1431_21116_17001_20883_20930; PSINO=5; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E5%BC%A0%E5%AD%A6%E5%8F%8B%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm',
}
# 获取爬取信息
word = raw_input('请输入要爬取照片名称：')
rn = raw_input('请输入要爬取照片个数：')
# 配置url
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word=%s&rn=%s'%(word, rn)

request = urllib2.urlopen(url)

response = request.read()

#print(type(response))  # json字符串格式
import json
msg = json.loads(response)  # 将json字符串格式转化为字典格式
# print(type(msg))  # dict
data = msg['data']
# print(type(data)) # list
# url = data[0]['hoverURL']
# print(url)
print data
a = 0
try:
    for it in data:
        if it:
            a += 1
            request = urllib2.urlopen(it['hoverURL'])
            with open('./django/img_%s.jpg'%a, 'wb') as f:
                f.write(request.read())
except Exception, e:
    print(e)




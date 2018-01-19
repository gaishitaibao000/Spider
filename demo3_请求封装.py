# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/9 11:45'
'''
访问url:http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
请求参数：
    i	hello
    from	AUTO
    to	AUTO
    smartresult	dict
    client	fanyideskweb
    salt	1515466801319
    sign	78f918a6eb55b77d633cba89bd8385da
    doctype	json
    version	2.1
    keyfrom	fanyi.web
    action	FY_BY_REALTIME
    typoResult	false
'''
import urllib2, urllib, random

headers = {
    'Host': 'fanyi.youdao.com',
    'Connection': 'keep-alive',
    'Content-Length': 214,
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://fanyi.youdao.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://fanyi.youdao.com/',
    #'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'P_INFO=m18937506461_2@163.com|1513604431|0|other|00&99|null&null&null#hen&410100#10#0#0|189461&1||18937506461@163.com; OUTFOX_SEARCH_USER_ID=-1882192054@123.160.224.62; JSESSIONID=aaazF_jFHgixVhhzngzdw; OUTFOX_SEARCH_USER_ID_NCOO=220777162.3335792; ___rl__test__cookies=1515474097581'
}

# 封装请求User-agent
ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]
user_agent = random.choice(ua)

# 定义url地址
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

import time
# 定义client
E = 'fanyideskweb'
# salt盐值
r = str(time.time()*1000 + random.randint(1, 10))
# 获取要翻译的字段
n = raw_input('请输入要翻译的字段：')
# JS获取的加密混淆码
O = 'aNPG!!u6sesA>hBAW1@(-'
# 确定sign参数
import hashlib
sign = hashlib.md5(E + n + r +O).hexdigest()

# 定义请求表单数据
form_data = {
    'i': n, # 要翻译的词语
    'from': 'AUTO', # 词语翻译之前的语言
    'to': 'AUTO', # 词语翻译之后的语音
    'smartresult': 'dict', # 数据类型
    'client': 'fanyideskweb', # 客户端标识
    'salt': r, # 反爬虫机制
    'sign': sign, # 反爬虫机制
    'doctype': 'json', # 数据类型
    'version': 2.1, # 版本号
    'keyfrom': 'fanyi.web', # 关键字
    'action': 'FY_BY_REALTIME', # 行为描述
    'typoResult': False # 结果类型
}
data = urllib.urlencode(form_data)


# 封装请求对象
request = urllib2.Request(url, data=data, headers=headers)

response = urllib2.urlopen(request)

print(response.read())
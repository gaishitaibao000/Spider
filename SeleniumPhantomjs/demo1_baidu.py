# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/15 15:52'

# 引入测试模块
from selenium import webdriver

# 启动phantomjs无界面浏览器
driver = webdriver.PhantomJS()

# 访问百度首页
driver.get('http://www.baidu.com')

# 获取百度的搜索输入框
keyword = driver.find_element_by_id('kw')
# 向输入框中输入一个要搜索的词语
keyword.send_keys(u'大清帝国')

# 查看浏览器截图
# driver.save_screenshot('baidu.png')

# 开始搜索：点击百度搜索按钮
btn = driver.find_element_by_id('su').click()

# 查看截图
driver.save_screenshot('baidu1.png')


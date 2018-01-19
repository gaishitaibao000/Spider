# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/16 21:34'

from selenium import webdriver
import time
# 引入配置对象DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
# 选一个浏览器头，伪装浏览器
dcap['phantomjs.page.setting.userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# 不载入图片，爬页面速度会快很多
dcap['phantomjs.page.setting.loadImages'] = False
# 设置代理
service_args = ['--proxy=123.128.117.235:8118', '--proxy-type=socks5']
# 打开带配置信息的phantomJS浏览器
driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
# 隐式等待5秒，可以自己调节
driver.implicitly_wait(5)
# 设置10秒页面超时返回，类似于request.get()的timeout选项，driver.get()每页timeout选项
# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题
driver.set_page_load_timeout(10)
# 设置10秒脚本超时时间
driver.set_script_timeout(10)

driver = webdriver.PhantomJS()
print('*********1')
driver.get('https://www.lagou.com')
driver.delete_all_cookies()
driver.add_cookie({'user_trace_token':'20171223160604-1f4b9966-e7b8-11e7-9e15-5254005c3644','LGUID':'20171223160604-1f4b9c84-e7b8-11e7-9e15-5254005c3644','index_location_city':'%E5%85%A8%E5%9B%BD','_ga':'GA1.2.1604755545.1514016364','_ga':'GA1.3.1604755545.1514016364','JSESSIONID':'ABAAABAAAHAAAFD4BD53098FA40B58423F55245A641D375','Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1515569426,1515831205,1516149887,1516149934','X_HTTP_TOKEN':'c760c6b9d06b13746e2583202be3b25d','TG-TRACK-CODE':'undefined','ab_test_random_num':'0','_gat':'1','LGSID':'20180117163107-c3bcc502-fb60-11e7-a1b4-525400f775ce','PRE_UTM':'','PRE_HOST':'','PRE_SITE':'','PRE_LAND':'https%3A%2F%2Fwww.lagou.com%2F','gate_login_token':'5a66babf046d763feec9942a7c1f62a6da56e8387f952c0b','login':'false','unick':'','_putrc':'','Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6':'1516177875', 'LGRID':'20180117163113-c755a69d-fb60-11e7-a1b4-525400f775ce'})
print('*********2休息一下马上回来')
driver.get('https://www.lagou.com')
driver.maximize_window()
# print('*********3')
print('*********4')
driver.find_element_by_id('cboxClose').click()
time.sleep(6)
driver.find_element_by_id('search_input').send_keys(u'爬虫')
driver.find_element_by_id('search_button').click()

print('*********5休息一下马上回来')
time.sleep(2)
# driver.save_screenshot('lg3.png')
# print(driver.find_elements_by_css_selector('.input_item .input'))
driver.find_elements_by_css_selector('.input_item .input')[0].clear()
driver.find_elements_by_css_selector('.input_item .input')[0].send_keys('18937506461')
driver.find_elements_by_css_selector('.input_item .input')[1].clear()
driver.find_elements_by_css_selector('.input_item .input')[1].send_keys('asd123')
driver.find_elements_by_css_selector('.input_item .btn')[0].click()
# print('*********6休息一下马上回来')
time.sleep(6)
driver.save_screenshot('lg4.png')
driver.quit()



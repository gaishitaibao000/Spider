# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/15 16:26'

# 引入测试模块
from selenium import webdriver

# 使用无界面浏览器
driver = webdriver.Chrome()

driver.get('http://qzone.qq.com')
# driver.maximize_window()
driver.switch_to_frame('login_frame')
# 切换到账号密码登录页面
# print driver.find_element_by_id('switcher_plogin')
# driver.save_screenshot('QQ.png')

driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('1353743652')
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('gaishitaibao000')
driver.find_element_by_id('login_button').click()
import time
time.sleep(3)
# driver.save_screenshot('QQ1.png')
height = 0
for num in range(1, 3):
    time.sleep(3)
    height = num * 5000
    driver.execute_script("window.scrollTo(0,{})".format(height))
time.sleep(3)
feed_friend_list = driver.find_elements_by_css_selector('.f-single')
time.sleep(3)
print(feed_friend_list)
for feed_friend in feed_friend_list:
    # print(feed_friend.find_element_by_xpath("//a[@class='f-name']"))
    # print(feed_friend.find_element_by_xpath("//div[@class='f-info']"))
    if feed_friend.find_element_by_css_selector('.f-name').text:
        print feed_friend.find_element_by_css_selector('.f-name').text
    time.sleep(3)
    if feed_friend.find_element_by_css_selector('.f-info').text:
        print feed_friend.find_element_by_css_selector('.f-info').text

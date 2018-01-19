# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/8 21:35'

import datetime,time
import urllib2


# 读取页面
def loadPage(url, filename):
    print filename + '正在下载'
    response = urllib2.urlopen(url)
    return response.read()


# 写入页面
def writePage(html, dirname, filename, kw):
    print filename + '正在保存'
    # time_now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # time_now = str(time_now)
    new_name = filename.decode('utf-8').encode('GBK')
    with open('./{0}/{1}'.format(dirname, new_name), 'w') as f:
        f.write(html)


# 遍历每页
def tiebaSpider(kw, begin_page, dirname, end_page):
    print '正在爬取'+kw
    for num in range(int(begin_page), int(end_page)+1):
        page_num = num*50
        filename = '第'+str(num)+'页.html'
        url = 'https://tieba.baidu.com/f?kw=%s&ie=utf-8&pn=%s'%(kw, page_num)
        html = loadPage(url, filename)
        writePage(html=html, dirname=dirname, filename=filename, kw=kw)
    print kw + '爬取完成'


if __name__ == '__main__':

    start = time.clock()
    # 获取爬取，保存信息
    kw = raw_input('请输入要爬取的贴吧名称：')
    begin_page = raw_input('请输入起始页：')
    end_page = raw_input('请输入终止页：')
    dirname = raw_input('请输入要保存文件的文件夹名称：').decode('utf-8').encode('gbk')

    import os
    path = os.path.dirname(__file__)
    os.mkdir('{0}/{1}'.format(path, dirname))
    print '****************'
    print dirname
    print path

    tiebaSpider(kw=kw, dirname=dirname, begin_page=begin_page, end_page=end_page)

    listdir = os.listdir('./{}/'.format(dirname))
    dir_size = sum(map(lambda x:os.path.getsize('./{}/'.format(dirname)+x),[file for file in listdir]))/1024
    print str(dir_size) + 'k'

    # 获取本地时间，消耗时间
    time_diss = time.clock() - start
    print '消耗了'+str(time_diss)
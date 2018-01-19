# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/11 20:13'
'''
用多线程爬取队列爬取百度照片
'''

import requests, threading, Queue, datetime, re, json

start_time = datetime.datetime.now()

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}
proxies = {
    'https':'39.88.41.99:8118',
    'http':'171.39.41.251:8123'
}

# 创建队列对象
url_queue = Queue.Queue()
for url_num in range(1, 3):
    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&word=%E5%BC%A0%E5%AD%A6%E5%8F%8B&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&step_word=%E5%BC%A0%E5%AD%A6%E5%8F%8B&pn=0&rn={}&gsm=96&1515673327194='.format(str(url_num))
    url_queue.put(url)

# 创建多线程锁
lock = threading.Lock()

def spider(urlqueue):
    while urlqueue.qsize() > 0:
        if lock.acquire():
            url = urlqueue.get()
            print('剩余未爬取量：%s当前线程：%s'%(urlqueue.qsize(), threading.currentThread().name))
            response = requests.get(url, headers=headers)
            response.encoding = 'utf-8'
            text_response = response.text
            json_response = json.loads(text_response)
            data = json_response['data']
            for msg in data:
                if msg:
                    img_url = msg['replaceUrl'][1]['ObjURL']
                    img = requests.get(img_url)
                    dir_name = '百度照片_张学友'.decode('utf-8').encode('gbk')
                    img_name = img_url[-20:].replace('/', '_')
                    with open('./{}/{}'.format(dir_name, img_name), 'wb') as f:
                        f.write(img.content)
                        print('%s储存完成'%url)
            lock.release()

if __name__ == '__main__':
    # 声明一个变量，保存多线程
    threads = []
    # 声明一个变量，控制启动多少个程序
    thread_num = 3
    # 创建线程对象，并启动线程
    for th in range(0, thread_num):
        # 创建线程对象
        current_thread = threading.Thread(target=spider, args=(url_queue,))
        current_thread.start()
        threads.append(current_thread)
    for t in threads:
        t.join()
    print('程序执行结束')



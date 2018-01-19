# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/11 11:27'

import requests, Queue, threading

# 创建一个保存url地址的LILO(FIFO)队列
url_queue =  Queue.Queue()
# 多线程锁
lock = threading.Lock()
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
}

for num in range(2):
    page_num = num*50
    url_queue.put('https://tieba.baidu.com/f?kw=%E8%B4%B4%E5%90%A7&ie=utf-8&pn='+str(page_num))

dirname = '多线程'.decode('utf-8').encode('gbk')
def spider(urlqueue):  # urlqueue参数变量
    while urlqueue.qsize() > 0:
        if lock.acquire():
            url = urlqueue.get()
            print('剩余线程：%s线程%s开始对%s爬取'%(urlqueue.qsize(), threading.currentThread().name, url))
            response = requests.get(url, headers=headers)
            with open('./%s/%s'%(dirname, num), 'w') as f:
                print('开始储存%s'%num)
                f.write(response.text.encode('utf-8'))

            # 解锁
            lock.release()


if __name__ == '__main__':
    # 声明一个变量，保存多线程
    threads = []
    # 声明一个变量，控制启动多少个线程
    threads_num = 3
    # 创建线程对象，并启动线程
    import datetime
    start_time = datetime.datetime.now()
    for ct in range(0, threads_num):
        current_thread = threading.Thread(target=spider, args=(url_queue, ))
        current_thread.start()
        threads.append(current_thread)
    print('##########################')
    # 让所有的线程join，就是让主线程等待所有子线程运行结束后推出
    for t in threads:
        t.join()
    end_time = datetime.datetime.now()
    use_time = (end_time-start_time).seconds

    import os
    print('开始计算大小')
    file_list = os.listdir('./%s'%dirname)

    print(sum(map(lambda x:os.path.getsize('./%s/%s'%(dirname, x)),[file for file in file_list]))+'k')
    print('消耗时间%ss'%use_time)



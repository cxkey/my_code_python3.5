from gevent import monkey;
import gevent
# import urllib2
import requests
import time
from threading import Thread

#有IO才做时需要这一句
monkey.patch_all()
import threading

def myDownLoad(url):
    while True:
        print('GET: %s' % url)
        resp = requests.get(url)
        data = resp
        print(data, url)
        time.sleep(0.1)

# gevent.joinall([
#         gevent.spawn(myDownLoad, 'http://www.fdfkjkd.com/'),
#         gevent.spawn(myDownLoad, 'http://www.jd.com'),
#         gevent.spawn(myDownLoad, 'http://www.baidu.com'),
# ])

def task():
    while True:
        print(1)
        time.sleep(2)
t = Thread(target=task)
t.start()
print(2)

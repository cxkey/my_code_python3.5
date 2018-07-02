import requests
import time
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado import gen
import json
import urllib

@gen.coroutine
def asyc_http_get_request(url, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    try:
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch(url, headers=headers)
        # res = json.loads(response.body)
        res = response
    except Exception as e:
        print(e)
        raise gen.Return({"status":"fail","msg":e})
    raise gen.Return(res)

@gen.coroutine
def get_response(address):
    try:
        r = yield asyc_http_get_request(address,None)
    except Exception as e:
        raise e
    finally:
        raise gen.Return(r)

@gen.coroutine
def main():
    addresses = ['http://www.fdfkjkd.com/', 'http://www.jd.com','http://www.baidu.com',]
    for address in addresses:
        # r = requests.get(address)
        r = yield get_response(address)
        print(r,address)

if __name__ == '__main__':
    IOLoop.instance().add_callback(main)
    IOLoop.instance().start()


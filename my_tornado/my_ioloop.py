
from tornado.ioloop import IOLoop
def my_timeout():
    print('timeout')
def my_callback():
    print('callback')
IOLoop.instance().add_timeout()
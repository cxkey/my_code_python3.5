import logging
import requests
LOGLEVEL = logging.DEBUG
# logging.getLogger("urllib3").setLevel(LOGLEVEL)
# logging.info('tesat')
# logging.getLogger("requests").setLevel(LOGLEVEL)
# r = requests.get('http://www.baidu.com')
a= logging.getLogger('test')
a.setLevel(LOGLEVEL)
logging.getLogger('test').addHandler(logging.FileHandler('test.log'))
a.info('test')
logging.getLogger('test').info('test2')
import logging
# logging.basicConfig()
# test = logging.getLogger('ts')
# test.setLevel(logging.DEBUG)
# print(test.handlers)
# # test.propagate = False
# test.info('test')
import sys

LOGLEVEL = logging.DEBUG
LOGFORMAT = '%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s'
logging.basicConfig(level=LOGLEVEL, format=LOGFORMAT,propagate=False)

test = logging.getLogger('test')
handler = logging.FileHandler('./test.log')
test.addHandler(handler)
handler = logging.StreamHandler(stream=sys.stdout)
test.addHandler(handler)

test.debug('test')


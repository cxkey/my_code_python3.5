import logging
import os
from logging.handlers import TimedRotatingFileHandler
alogger = logging.getLogger('action')
path = './'
LOGFORMAT = '[%(asctime)s] %(levelname)s %(module)s:%(lineno)d %(message)s'
handler = logging.handlers.TimedRotatingFileHandler('{}{}{}.log'.format(path, os.sep, alogger.name),
                                                    when='midnight', interval=1, backupCount=5)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(LOGFORMAT)
handler.setFormatter(formatter)
alogger.addHandler(handler)
try:
    a = 2/0
except Exception as e:
    alogger.exception(e)

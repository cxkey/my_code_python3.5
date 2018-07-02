import logging
from logging.handlers import TimedRotatingFileHandler
import os


def get_logger(name, path=None, _level=logging.DEBUG, is_stdout=True):
    _format = '[%(asctime)s] %(levelname)s %(module)s:%(lineno)d %(message)s'
    if not path:
        path = os.path.dirname(os.path.abspath(__file__))
    logger = logging.getLogger(name)
    if logger.handlers:
        print('haha')

    # handler = logging.handlers.TimedRotatingFileHandler('{}{}{}.log'.format(path, os.sep, logger.name),
    #                                                     when='midnight', interval=1, backupCount=10)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(path+os.sep+logger.name,mode='w')
    # handler.setLevel(_level)
    formatter = logging.Formatter(_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    #
    # if is_stdout:
    #     handler = logging.StreamHandler(sys.stderr)
    #     handler.setLevel(level)
    #     formatter = logging.Formatter(format)
    #     handler.setFormatter(formatter)
    #     logger.addHandler(handler)
    return logger

log = get_logger('dfdfdf')
for i in range(10):
    log.warn('test1')
# log.info('test2')
# log.warning('test3')

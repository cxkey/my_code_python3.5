import datetime
from collections import defaultdict


def date_range( start, end, step=1, format="%Y/%m/%d"):
    strptime, strftime = datetime.datetime.strptime, datetime.datetime.strftime
    if isinstance(start, str):
        start = strptime(start, format)
    if isinstance(end, str):
        end = strptime(end, format)
    days = (end - start).days
    return [(start + datetime.timedelta(i)).date() for i in range(0, days+1, step)]
print(date_range('2018/06/10','2018/06/20'))


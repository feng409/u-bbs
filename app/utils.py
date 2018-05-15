# coding: utf-8
import time
import re


def log(*args, **kwargs):
    """
    代替print，自定义打印
    [2018/05/12 21:16:58] ...
    """
    format_date = format_time(time.time())
    print('[{}]'.format(format_date), *args, **kwargs)


def format_time(timestamp):
    """
    格式化时间
    :param timestamp: time.time()
    :return: [2018/05/12 21:16:58]
    """
    time_tuple = time.localtime(int(timestamp))
    format_date = time.strftime('%Y/%m/%d %H:%M:%S',
                                time_tuple)
    return format_date


def validate_email(email):
    return re.match(r'^[\w-]+(\.[\w-]+){0,4}@[\w-]+(\.[\w-]+){1,4}$', email)


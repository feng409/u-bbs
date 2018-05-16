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


class Elapse:
    minute = 60
    hour = 60 * 60
    day = 60 * 60 * 24


def moment(passed):
    """
    xxx秒前
    :param passed: time.time()
    :return: str xxx[秒分时天]
    """
    now = time.time()
    elapse = now - passed
    if elapse < Elapse.minute:
        word = '{}秒前'.format(int(elapse))
    elif Elapse.minute < elapse < Elapse.hour:
        word = '{}分钟前'.format(int(elapse / Elapse.minute))
    elif Elapse.hour < elapse < Elapse.day:
        word = '{}小时前'.format(int(elapse / Elapse.hour))
    else:
        word = '{}天前'.format(int(elapse / Elapse.day))
    return word

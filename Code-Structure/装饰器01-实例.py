#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 11:32
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 装饰器01-实例.py
# @Software: PyCharm


import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()
print('------')





def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')
    print('------')


today()
print(today.__name__)
print('------')
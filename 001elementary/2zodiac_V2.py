#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Jianfeng Ding  Time: 2018/11/13

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# (month, day) = (2, 15)
#
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# print(zodiac_day)
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])  # 将列表作为下标


int_month = int(input("Please input Month:"))
int_day = int(input("Please input Day:"))
print(type(int_month))
# 元组取长度,以列表作为下标
# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 23:
#         print(zodiac_name[0])
#         break

n = 0
while zodiac_days[n] < (int_month, int_day):
    if int_month == 12 and  int_day > 23:
        break
    n += 1
print(zodiac_name[n])


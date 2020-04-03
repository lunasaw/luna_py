# -*- coding:utf-8 -*-
# @Time: 2020/4/1 17:23
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_1_datetime.py

'''
	datetime()模块
	time 时间
	date 日期 data 数据
	datetime 日期时间
	timedelta 时间差
'''
import datetime
import time

print(datetime.time.hour)  # 得到对象
print(time.localtime().tm_hour)  # 得到具体属性值

date = datetime.date(2020, 4, 1)  # 用于生成一个指定的时间,年月日
print(date)
print(date.day)
print(datetime.date.ctime(date))

# datetime.timedelta
print(datetime.date.today())  # 返回当前的年日月=>底层用time构造,封装了time的一些方法

timedel = datetime.timedelta(days=1, hours=2)  # 获取两个小时的时间

print(timedel)

now = datetime.datetime.now()
print(now)

print(now - timedel)  # 获取时间差值

# -*- coding:utf-8 -*-
# @Time: 2020/4/1 14:25
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_1_time.py

# time 模块

import time

print(time.time())  # 返回自纪录时间来的时间值

time.sleep(1)  # 睡1秒

print(time.time())

# 将时间转为字符串
print(time.ctime(time.time()))

# 时间戳转为元组
t = time.localtime(time.time())
print(t)

# 将元组转为时间戳 去掉了精度值
print(time.mktime(t))

# 将元组的时间转为字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", t))

# 将字符串转为元组
s = time.strptime('2020/04/01', '%Y/%m/%d')
print(s)

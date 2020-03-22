# -*- coding:utf-8 -*-
# @Time: 2020/3/23 1:14
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_23_except.py

try:
	b = 1 / 0
except BaseException:
	print("这是一个异常噢!")

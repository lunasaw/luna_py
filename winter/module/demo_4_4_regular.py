# -*- coding:utf-8 -*-
# @Time: 2020/4/4 22:50
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_4_regular.py

# 分组 匹配0-100 数组
import re

n = '300'
max = re.match(r'[1-9]?\d?|100$', n)  # | 或者符号
print(max)

email = "12312312@qq.com"
email = re.match(
	r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$',
	email)
print(email)

idcard = "300384199911082312"
idcard = re.match(r'^[1-9]\d{5}(?:18|19|20)\d{2}(?:(?:0[1-9])|(?:1[0-2]))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$',
                  idcard)
print(idcard)

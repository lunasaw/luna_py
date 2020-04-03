# -*- coding:utf-8 -*-
# @Time: 2020/4/3 22:20
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_3_pillow.py

# 第三方模块

import requests
import PIL  # pillow已不维护 改为PIL

reponse = requests.get("http://iszychen.club")
# print(reponse.text)

# 正则 re 模块
import re

msg = "luna"  # <== 待过滤的字符串
pattern = re.compile("l")  # 正则
find = pattern.match(msg)  # match从头开始匹配 返回一个Match对象
print(find)

# 使用正则模块

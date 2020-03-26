# -*- coding:utf-8 -*-
# @Time: 2020/3/27 0:25
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_27_module.py

import math as m

# help(math)
print(m.e)
print(m.sin(m.pi / 2))
print(id(m))

import math  # 模块无论加载多少次 都是指向同一个对象 相同引入只会执行一次

print(id(math))

# from .. import   引入模块中的成员
from math import *  # 引入全部  可直接使用内容用

from math import sin as Sin

print(Sin(0))

# 动态导入 使用 importlib 但是 这个模块可以在此引入reload

import importlib

a = importlib.import_module("math")
print(a.pi)
importlib.reload(math)  # 但是 这个模块可以在此引入reload

# -*- coding:utf-8 -*-
# @Time: 2020/3/27 0:43
# @Author: luna
# @Email: 15696756582@163.com
# @File: __init__.py.py

'''
import xxx
from xxx import xxx
from xxx import * + __all__ = []  from 包名 import *
__name__ 自己 __name__ 别的模块 __模块名__

包:
	user
		|-- __init__.py  导入包默认执行该文件
		|-- xxx,py
		|-- xx.py
			|-- add()

	article
		|-- aa.py

	bb.py

		from user.xx import add
		add()

	循环导入：
		1. 重构代码
		2. 将导入语句放入函数
		3. 导入语句放到模块后

	系统：
		sys：
		sys.path  sys.version sys.argv
'''

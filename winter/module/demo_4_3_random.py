# -*- coding:utf-8 -*-
# @Time: 2020/4/3 21:35
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_3_random.py

import random

print(random.random())  # 0~ 1 之间的随机小数
print(random.randrange(1, 10))  # 指定范围内的随机整数
print(random.randrange(1, 10, 2))  # 指定间隔,步长整数
print(random.randint(1, 10))  # 包含范围在内的随机数

list = ['张三', '李四', '王五', '小六']
ran = random.choice(list)  # 随机抽出指定列表里的某个值
print(ran)

random.shuffle(list)  # 将列表顺序打乱
print(list)


# 验证码
def func():
	code = ''
	for i in range(4):
		randomOne = str(random.randint(0, 9))
		randomTwo = chr(random.randint(65, 90))  # chr ascll 转换
		randomThree = chr(random.randint(97, 122))
		code += random.choice([randomOne, randomTwo, randomThree])
	return code


code = func()
print(code)

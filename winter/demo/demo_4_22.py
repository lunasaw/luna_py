# -*- coding:utf-8 -*-
# @Time: 2020/4/22 15:51
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_4_22.py
import math

radius = eval(input('请输入圆的半径：'))
area = math.pi * pow(radius, 2)
length = 2 * math.pi * radius
print('面积：{}，周长：{}'.format(area, length))

# score = int(input("请输入一个成绩"))
# if (score >= 90):
# 	print("优秀")
# elif (score >= 80):
# 	print("良好")
# elif (score >= 70):
# 	print("一般")
# elif (score >= 60):
# 	print("及格")
# else:
# 	print("不及格")

# -*- coding:utf-8 -*-
# @Time: 2020/3/23 1:14
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_23_except.py

try:
	b = 1 / 0
except BaseException:
	print("这是一个异常噢!")

# 多个异常 子类=>父类 依次捕捉
try:
	a = input("请输入一个被除数: ")
	b = input("请输入一个除数: ")
	c = float(a) / float(b)
	print(c)
except ZeroDivisionError:
	print("异常, 除数不能为0")
except ValueError:
	print("不能将字符转为数字")
except NameError:
	print("变量不存在")
except BaseException as e:
	print(e)

# _else 结构 try 如果异常执行异常 无异常执行else

try:
	a = input("请输入一个被除数: ")
	b = input("请输入一个除数: ")
	c = float(a) / float(b)
except BaseException as e:
	print(e)
else:
	print(c)
	print("我是else 程序结束")

# finally  无论是否发生异常都执行 关闭try中打开的操作

try:
	a = input("请输入一个被除数: ")
	b = input("请输入一个除数: ")
	c = float(a) / float(b)
except BaseException as e:
	print(e)
else:
	print(c)
finally:
	print("我是finally 程序结束")

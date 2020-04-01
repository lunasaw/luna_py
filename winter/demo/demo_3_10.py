# -*- coding:utf-8 -*-
# @Time: 2020/3/10 11:56
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_10.py

# lambda 表达式
f = lambda a, b, c: a + b + c
print(f)
print(f(1, 2, 3))

g = [lambda a: a + 2, lambda b: b + 3, lambda c: c * 5, f]
v = [1, 2, 3]
print(v[1])
print(g[0](6), g[1](8), g[3](1, 2, 3))

# 测试eval()
eval("print('hello world')")
q = 10
w = 20
e = eval("q + w")
print(e)

dictEval = dict(q=100, w=200)
d = eval("q + w")
print(d)
# 赋给定范围内取值
d = eval("q + w", dictEval)
print(d)


# 递归
def factorial(n):
	if n == 1:
		return 1
	return n * factorial(n - 1)


fac = factorial(4)
print(fac)


# 内部嵌套函数
def fun1():
	print("fun1")

	def fun1_1():
		print("内部函数")

	fun1_1()


fun1()

# fun1_1找不到  只能在内部使用
#  全局变量 global  内部声明外部函数变量 nonlocal

a = 100


def func():
	b = 100

	def func_1():
		# 声明外部函数的局部变量  作用于上一层函数
		nonlocal b
		b = 200

		# 声明为全局后可以使用 但不能在内部定义外部可以使用的  只能内部声明而使用外部  或者外部直接声明为全局 内部也可使用
		global a
		a = 20

	func_1()
	print(b)


func()
print(a)

# LEGB local > enclosed >global > built in(python 自定义变量)

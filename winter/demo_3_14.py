# -*- coding:utf-8 -*-
# @Time: 2020/3/14 15:54
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_14.py

#  测试 super

class A:
	def say(self):
		print("A:", self)


class B(A):
	def say(self):
		# A.say(self)
		super().say()
		print("B:", self)


B().say()


# 多态 对象的继承和重载实现
class Man:
	def eat(self):
		print("饿了, 想吃饭")


class Chinese(Man):
	def eat(self):
		print("中国人用筷子")


class Engaged(Man):
	def eat(self):
		print("英国人用刀叉")


def manEat(m):
	if isinstance(m, Man):  # 只要m 是Man 或者Man 的子类都执行
		m.eat()
	else:
		print("不能吃饭")


manEat(Chinese())
manEat(Engaged())

e = Chinese()

print(e.__dict__)  # 打印属性
print(e.__class__)  # 打印所属类
print(Chinese.__bases__)  # 打印父类
print(Chinese.mro())  # 所有向上索引
print(Man.mro())
print(Man.__subclasses__())  # 打印所有子类
print(e.__dir__())  # 所有属性
print(e.__doc__)  # 解释文档
print(e.__sizeof__())  # 占用字节

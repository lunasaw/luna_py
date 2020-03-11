# -*- coding:utf-8 -*-
# @Time: 2020/3/11 20:27
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_11.py

class Student:
	score = 0  # 类属性

	def __init__(self, name, age):  # self 必须在第一个参数
		self.name = name  # 实例属性
		self.age = age

	# 类方法 和静态方法 不能调实例变量  实例方法 (磨具有了  没有实例化的时候)
	@classmethod  # classmethod 类方法 操作类属性 new 类的同时创建方法
	def doIt(cls):  # cls 指类对象 用于类方法第一个参数
		print(str(cls.score) + "先调用此方法")

	@staticmethod  # 静态方法
	def doGet(cls):
		print(cls)
		print(cls.name)
		print("这是一个静态方法")

	def sayAge(self):  # 普通实例方法
		print("{0}的年龄是: {1}".format(self.name, self.age))


# 实例化类时 new 一个  然后init
b = Student("李诗琪", 18)
a = Student(None, 18)
a.doIt()
a.sayAge()
a.score = 80
print(a.score)

a.doGet(b)

# 类的传递
stu = Student
v = stu("李诗琪", 18)
v.sayAge()


# 定义 __call__ 方法的对象 称为可调用对象 对象可像函数一样调用
class SalaryAccount:
	'''工资计算类== 定义了call的可以直接调用'''

	def __call__(self, salary):  # * 元组  ** 字典
		print("算工资啦")
		yearSalary = salary * 12
		daySalary = salary / 22.5
		hourSalary = daySalary / 8
		return dict(yearSalsry=yearSalary, monthSalary=salary, daySalary=daySalary, hourSalary=hourSalary)


s = SalaryAccount()
print(s(4500))


# python 没有方法重载 Java 可以通过形参列表区分 但是python没有参数类型区分 是自动分配的 故无法区分 ==>>定义多个同名方法时  只有最后一个有效

# 测试方法的动态性
class Person:

	def work(self):
		print("努力上班")


def playGame(s):
	print("{0}在玩游戏".format(s))


# 将方法作为对象赋值给属性 使其也具有这个方法
Person.play = playGame
p = Person()
p.play()

# 私有属性 和私有方法
'''
	两个 __ 开头的属性 是私有的 
	两个 __ 开头的方法 是私有的  ==> 作为一种约定  类外部不能直接访问私有属性(方法)   可以通过类名调用

'''


class Employee:

	def __init__(self, name, age):
		self.name = name
		self.__age = age  # 私有属性

	@property
	def getAge(self):
		return self.__age

	@getAge.setter
	def setAge(self, age):
		if 0 < age < 100:
			self.__age = age
		else:
			print("输入有误")

	def __toString(self):  # 私有方法
		print("{0}的年龄是{1}".format(self.name, self.__age))  # 内部可以调用


e = Employee("陈章月", 18)

print(e.name)
print(dir(e))
# print(e.age)
print(e._Employee__age)  # 外部访问私有属性
# e .__toString()
e._Employee__toString()

# @property 装饰器
print("property 装饰器 类似将方法转为属性  不需要括号")
print(e.getAge)
e.setAge = 80
print(e.getAge)

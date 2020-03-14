# -*- coding:utf-8 -*-
# @Time: 2020/3/13 23:55
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_13.py

# 继承

class Person:
	def __init__(self, name, age):
		print("调用父类构造")
		self.__name = name
		self.age = age

	def sayAge(self):
		print("这里是打印年龄的方法")


class Student(Person):
	def __init__(self, name, age, score):
		Person.__init__(self, name, age)  # 子类的覆盖初始化必须在此调用父类初始化方法   Java中类似 默认super自动调用
		self.score = score

	def sayAge(self):
		print("这里覆盖了父类的方法")

	def sayName(self):
		print("这里调用父类属性" + self._Person__name)  # 私有属性不能调用  self.__name ==> self._Person__name

	def sayScore(self):
		print(self.score)

	def __str__(self):
		return "重写了str方法"


print(Student.mro())  # 打印继承过程
s = Student("陈章月", 20, 80)
s.sayAge()
s.sayName()
s.sayScore()

print("dir()查看对象的属性" + str(s.__dir__()))
# age, name, score是属性    sayName  sayAge  也是属性  只是他俩的属性类型是method
print(type(s.sayAge))

print(s)


# 多继承 从左到右 依次覆盖掉

# 测试单例模式

class MySingleton:
	__obj = None
	__init__flag = True  # 标志 是否已经创建

	def __new__(cls, *args, **kwargs):
		if cls.__obj == None:
			cls.__obj = object.__new__(cls)

		return cls.__obj

	def __init__(self, name):
		if MySingleton.__init__flag:
			print("__init__")
			self.name = name
			MySingleton.__init__flag = False


a = MySingleton("aa")
print(a)
b = MySingleton("bb")
print(b)

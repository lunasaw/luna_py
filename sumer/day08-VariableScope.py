# 测试全局变量,局部变量
'''
def print_star(n):
    print("*"*n)

print(print_star)
print(id(print_star))
c = print_star
c(3)

a = 100
#全局变量
def f1():
    global a
#如果要在函数内改变全局变量的值，增加 global关键字声明 print(a) #打印全局变量a 的值
    a = 300
f1()
print(a)

a = 100
def f1(a,b,c):
    print(a,b,c)
print(locals())
#打印输出的局部变量
print("#"*20)
print(globals())
#打印输出的全局变量
f1(2,3,4)'''

import time

import math


def test01():
	start = time.time()
	for i in range(10000000):
		math.sqrt(30)
		end = time.time()
	print("耗时{0}".format((end - start)))


def test02():
	b = math.sqrt
	start = time.time()
	for i in range(10000000):
		b(30)
		end = time.time()
	print("耗时{0}".format((end - start)))


test01()
test02()

# -*- coding:utf-8 -*-
# @Time: 2020/3/9 14:09
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_9.py
import copy

# 传递不可变对象  产生了一个新的对象
a = 100


def fun(n):
	print("n:", id(n))
	n = n + 200
	print("n:", id(n))
	print(n)


fun(a)
print("a:", id(a))

# 浅拷贝  只拷贝引用  不拷贝内容


a = [10, 20, 30, [1, 2]]
b = copy.copy(a)
print("浅拷贝b" + str(b))
c = copy.deepcopy(a)
print("深拷贝c" + str(c))
b[3].append(20)
c[3].append(29)
print("修改b 影响a" + str(a))
print("修改c 不影响a" + str(c))


# 默认参数必须放普通参数后面

def fun1(q, w, e=1):
	print(q, w, e)


fun1(1, 2, 3)  # 个数不比配则报错
fun1(1, 2)


# 可变参数

def fun2(r, s, *t):  # *一个*表示一个元组  **表示一个字典
	print(r, s, t)


def fun3(u, v, **w):
	print(u, v, w)


fun2(1, 2, (1, 2, 3))
fun3(1, 2, name="chen", age=18)


# 强制命名参数 在可变参数后还需加参数 传入时 必须强制命名

def fun4(*x, y, z):
	print(x, y, z)


fun4((1, 2), y="强制命名", z="参数")

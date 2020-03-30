# -*- coding:utf-8 -*-
# @Time: 2020/3/24 0:01
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_24_except_finally.py

try:
	f = open("../doFile/a.txt", "r")
	content = f.readline()
	print(content)
except:
	print("文件未找到")
finally:
	print("我是finally 执行关闭资源")
	try:
		f.close()
	except:
		print("文件关闭失败")
print("程序结束")

# with 上下文管理器 文件被打开都会自行关闭
# 序列化
import pickle

with open(r"../doFile/b.dat", "rb") as m:
	b1 = pickle.load(m)
	b2 = pickle.load(m)
	b3 = pickle.load(m)
	print(b1)
	print(b2)
	print(b3)

# trackback 模块
import traceback

# try:
# 	print("step1")
# 	num = 1 / 0
# except:
# 	traceback.print_exc()  # 追溯异常信息

'''将异常信息输出到文件'''
try:
	print("step1")
	num = 1 / 0
except:
	with open("except.txt", "a") as f:
		traceback.print_exc(file=f)  # 追溯异常信息输入到文件  不在控制台报错

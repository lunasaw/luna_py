# -*- coding:utf-8 -*-
# @Time: 2020/3/16 22:54
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_16.py

# 二进制文件操作
with open(r"../guiTest/imgs/puke/puke3.gif", "rb") as f:
	with open("pukeCopy.gif", "wb") as w:
		for line in f.readlines():
			w.write(line)
	print("文件拷贝完成")
	# 常用属性
	print(f.mode)  # 返回打开模式
	print(f.name)
	print(f.tell())
# print(f.truncate(99))  # 只保留99个字节  多余的都删掉

# 序列化
import pickle

with open(r"b.dat", "wb") as  q:
	a1 = "陈章月"
	a2 = "12123"
	a3 = [11, 22, 33]

	pickle.dump(a1, q)
	pickle.dump(a2, q)
	pickle.dump(a3, q)

# 取出来
with open(r"b.dat", "rb") as m:
	b1 = pickle.load(m)
	b2 = pickle.load(m)
	b3 = pickle.load(m)

	print(b1)
	print(b2)
	print(b3)

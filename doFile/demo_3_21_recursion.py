# -*- coding:utf-8 -*-
# @Time: 2020/3/22 0:46
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_21_recursion.py

# 测试阶乘
def factorial(n):
	if n == 1:
		return n
	else:
		return factorial(n - 1) * n


print(factorial(6))

# 用递归打印目录和文件
import os

allFiles = []


def getAllFile(path, leval):
	childFiles = os.listdir(path)
	for file in childFiles:
		filePath = os.path.join(path, file)
		if os.path.isdir(filePath):
			getAllFile(filePath, leval + 1)
		allFiles.append("\t" * leval + filePath)
	# print("\t"*leval+filePath)


getAllFile("D:\myproject\pythonTest", 0)
for f in allFiles:
	print(f)

# -*- coding:utf-8 -*-
# @Time: 2020/3/20 0:17
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_19_os.path.py

# os.path 模块
import os
import os.path  # from os import path

'''文件外部属性'''
print(os.path.isabs("a.txt"))  # 判断是不是绝对路径
print(os.path.isdir("a.txt"))  # 是不是一个文件夹
print(os.path.isfile("a.txt"))  # 是不是一个文件
print(os.path.exists("a.txt"))  # 是否存在

'''文件基本信息'''
print(os.path.getsize("a.txt"))  # 获取文件大小
print(os.path.abspath("a.txt"))  # 获取绝对路径
print(os.path.dirname("D:/a.txt"))  # 父级卷名
print(os.path.getctime("a.txt"))  # 创建时间  返回毫秒级数字
print(os.path.getatime("a.txt"))  # 访问时间
print(os.path.getmtime("a.txt"))  # 修改时间

'''路径相关'''
path = os.path.abspath("a.txt")
print(os.path.split(path))  # 元组  左边父级路径 右边文件名称
print(os.path.splitext(path))  # 元组 按.切割
print(os.path.join("aa", "bb", "cc"))  # 路径链接

# practise  列出指定目录下所有的.py文件 并输出文件名
path = os.getcwd()
fileList = os.listdir(path)
for fileName in fileList:
	if fileName.endswith("py"):
		print(fileName)

print("====推导式====")
fileList2 = [fileName for fileName in os.listdir(path) if fileName.endswith("py")]
for f in fileList2:
	print(f, end="\t")

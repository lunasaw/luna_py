# -*- coding:utf-8 -*-
# @Time: 2020/3/15 12:21
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_15_file.py

# 文件
# 创建
f = open(r"a.txt", "w")  # r 表示资源路径 不需要转义
q = open(r"b.txt", "w", encoding="utf-8")  # 指定编码格式打开文件
'''
	r 读
	w 写 存在则覆盖 不存在则创建
	a append 存在在后面追加 不存在则创建
	b 二进制文件  字节操作  默认为文本文件
	+ 读写可用
'''
# 操作
print(f.name)
s = "这是一个文本文件"
f.write(s)
# writlines 将一个列表内容写入 不写入换行
r = ["陈章月", "李诗琪"]
q.writelines(r)
# 需自行写入换行
q.write("\n")
q.write(s)
# 关闭
f.close()
q.close()

# 异常处理
try:
	p = open(r"b.txt", "r", encoding="utf-8")
	print(p.tell())  # 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数)。
	print(p.seek(12, 0))  # 用来移动文件指针。偏移量: 单位为比特，可正可负  起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
	print(p.read(2))  # 读两个
	t = p.readlines()
	print(t)
except Exception as x:
	print(x)
finally:
	p.close()

# 读取每一行  # win 默认编码为gbk 所以需要指定编码格式  cmd 控制台  chcp 65001
""" 
with 语句实质是上下文管理。
1、上下文管理协议。包含方法__enter__() 和 __exit__()，支持该协议对象要实现这两个方法。
2、上下文管理器，定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。
3、进入上下文的时候执行__enter__方法，如果设置as var语句，var变量接受__enter__()方法返回值。
4、如果运行时发生了异常，就退出上下文管理器。调用管理器__exit__方法。　　
"""
with open(r"b.txt", "r", encoding="utf-8") as v:  # 但是with本身并没有异常捕获的功能，但是如果发生了运行时异常，它照样可以关闭文件释放资源。
	for a in v:
		print(a)

c = [" 你好 ", " 中国 "]
b = enumerate(c)  # 返回的是一个字典对象   带序号  需用list 转为字符串
print(list(c))
print(list(b))
r = [tmp.strip() + str(index) for index, tmp in enumerate(c)]
# strip 去首尾空白符
print(r)

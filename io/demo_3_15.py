# -*- coding:utf-8 -*-
# @Time: 2020/3/15 12:21
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_15.py

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
with open(r"b.txt", "r", encoding="utf-8") as v:
	for a in v:
		print(a)

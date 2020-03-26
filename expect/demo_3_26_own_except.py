# -*- coding:utf-8 -*-
# @Time: 2020/3/26 23:16
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_26_own_except.py

#  自定义异常

class AgeError(Exception):
	def __init__(self, errorInfo):
		Exception.__init__(self)
		self.errorInfo = errorInfo

	def __str__(self):
		return "年龄不符合:" + str(self.errorInfo)


'''测试'''
if __name__ == "__main__":  # 如果未true 则模块作为独立文件运行 可以作为测试模块
	age = int(input("请输入您的年龄"))
	if age < 1 or age > 200:
		raise AgeError(age)
	else:
		print("输入成功")

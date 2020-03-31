# -*- coding:utf-8 -*-
# @Time: 2020/3/31 23:00
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_31_GUI.py

'''测试一个经典的GUI程序'''
from tkinter import *
from tkinter import messagebox


class Application(Frame):  # 自定义组件

	def __init__(self, master=None):
		super().__init__(master)  # super() 调用父类的初始化方法
		self.master = master
		self.pack()
		self.createWidget()

	def createWidget(self):  # 创建更多组件
		self.btn = Button(self)
		self.btn["text"] = "点我送花"
		self.btn.pack()  # 画
		self.btn["command"] = self.give
		# 退出按钮
		self.btn02 = Button(self, text="退出")
		self.btn02["command"] = self.master.destroy()
		self.btn02.pack()

	def give(self):
		messagebox.showinfo("送花", "送你花花")


if __name__ == '__main__':
	root = Tk()  # 窗口 root 引用
	root.geometry("400x300+300+300")  # 窗口大小
	root.title("luna")  # 窗口标题

	app = Application(master=root)
	root.mainloop()

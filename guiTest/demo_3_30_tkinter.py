# -*- coding:utf-8 -*-
# @Time: 2020/3/30 22:51
# @Author: luna
# @Email: 15696756582@163.com
# @File: demo_3_30_tkinter.py

from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Luna 的 GUI")
root.geometry("500x300+100+200")  # 改变窗口  wxh 高x宽 +-x 屏幕左右距离 +-y  屏幕上下距离=> 距左边100 距上200
btn01 = Button(root)
btn01["text"] = "点我就送花"

btn01.pack()


def give(e):  # e是事件对象
	messagebox.showinfo("Message", "送你一朵花")
	print("送你99多花")


btn01.bind("<Button-1>", give)  # 绑定单击事件方法  鼠标左键单击Button-1
root.mainloop()  # 调用组件 进入循环

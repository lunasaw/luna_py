from tkinter import *
from tkinter import messagebox

root = Tk()  # 创建一个窗口

root.title("我的第一个gui程序")
root.geometry("500x300+100+200")  # 这里乘号 用x 不用* 表示大小加x,y 走向

btn01 = Button(root)
btn01["text"] = "点我送花"

btn01.pack()


def lendflower(e):  # e:事件对象
    messagebox.showinfo("Message", "送你一朵花")
    print("送你很多玫瑰花")


btn01.bind("<Button-1>", lendflower)  # 绑定单击事件方法
root.mainloop()  # 调用组建的mainloop() 方法 进入事件循环

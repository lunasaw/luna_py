'''
测试一个经典的GUI程序的写法 使用面向对象的方式

'''
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    '''一个经典的GUI程序'''
    pass

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义 不是父类对象
        self.master = master  # 构造
        self.pack()
        pass
        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        self.btn01 = Button(self)
        self.btn01["text"] = "点我送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        # 创建一个按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你一朵玫瑰花")


root = Tk()
root.geometry("400x200+200+300")
root.title("一个经典的GUI程序")
app = Application(master=root)
root.mainloop()

'''
测试一个经典的GUI程序的写法 使用面向对象的方式

'''
from tkinter import *


class Application(Frame):
    '''一个经典的GUI程序'''
    pass

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义 不是父类对象
        self.master = master  # 构造
        self.pack()  # 窗口显示
        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        self.label01 = Label(self, text="攻城狮", width=10, height=2,
                             bg="black", fg="white")
        self.label01.pack()
        # self.label01["text"] 可往上配置
        self.label02 = Label(self, text="zychen", width=10, height=2,
                             bg="black", fg="red", font=("黑体", 30))
        self.label02.pack()
        # 显示图像
        global photo  # 需要是全局变量 不然本方法执行后 图片消失
        photo = PhotoImage(file="imgs/a.gif")
        self.label03 = Label(self, image=photo)
        self.label03.pack()


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()

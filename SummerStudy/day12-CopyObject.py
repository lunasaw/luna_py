#测试对象的浅拷贝,深拷贝
import copy
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=cpu


class Cpu:
    def calculate(self):
        print("你算吗?")
        print("cpu对象:",self)

class Screen:
    def show(self):
        print("这是一张图!")
        print("screen对象",self)
'''
#测试赋值  变量指向同一个对象

m1=MobilePhone()
m2=m1
print(id(m1))
print(id(m2))
'''
#测试浅复制
c1=Cpu
c2=c1
print(c1)
print(id(c1))
print(id(c2))
s1=Screen
print(s1)
m1=MobilePhone(c1,s1)
m2=m1
#变量赋值时  指向同一个对象  故id相等
print(id(m1))
print(id(m2))
m2=copy.copy(m1)
#使用copy方法时 为浅拷贝  为m2变量开辟另一个内存空间 但是对象里面属性还是为同一个对象
print(id(m1))
print(id(m2))
print(m1,m1.cpu,m1.screen)
print(m2,m2.cpu,m2.screen)
#测试深拷贝
m3=copy.deepcopy(m1)
#深copy方法 deepcopy 不仅为m3变量赋值  另将对象里属性也另复制
print(m1,m1.cpu,m1.screen)
print(m3,m3.cpu,m3.screen)
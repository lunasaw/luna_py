'''类名守字母大写 多个单词用驼峰原则


'''
class Student:
    #__init__() 构造函数
    def __init__(self,name,score): #self 必须位于第一个参数 用于给对象赋初始值
       self.name=name
       self.score=score
    def say_score(self):
        print("{0}的分数是: {1}".format(self.name,self.score))
#类方法 操作类属性 实例方法操作实例对象
    @classmethod
    def stu(cls, name):
        print(name)
#静态方法 python中允许存在类中于类对象完全无关的方法 成为静态方法 需要通过类调用
    @staticmethod
    def stu(str):
        print(str)
#测试
s1=Student("陈章月",19)
s1.say_score()
s2=Student("王二",99)

print(s1.score)
stu=Student
# 把Student当作摸具 类似于java 的最大父类
s3=stu("张三",20)
print(s3.say_score())
s3.stu(s3.name)

#回收s1对象  当引用计数为0时 py会自动回收对象 析构方法
del s1
#print(s1.name)

#定义了__call__方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用。
class SalaryAccount:
    """工资计算类"""
    def __call__(self,salary):
        print("算工资啦...")
        yearSalary=salary*12
        daySalary=salary//22.5
        hourSalary=daySalary//8
#返回一个元组 用dict创建 关键字等于值
        return dict(yearSalary=yearSalary,daySalary=daySalary,hourSalary=hourSalary)
#直接调用该类里的__call__方法
s=SalaryAccount()
print(s(3000))

#py中没有方法的重载, java中有 是因为能通过形参列表来区分
# 但是py中没有类型 故无法区分重载方法 只能通过名字区分
# 多个方法重名是  只有最后一个存在
def playGame(self,str):
    print("{0}在玩游戏".format(str))
Student.play=playGame
person=Student("陈章月",19)
person.play(person.name)

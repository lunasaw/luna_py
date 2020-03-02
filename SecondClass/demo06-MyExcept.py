#自定义异常
class AgeError(Exception):#继承父类
    def __init__(self,errorInfo):#重写构造器
        Exception.__init__(self) #调用父类构造
        self.errorInfo=errorInfo
    def __str__(self):
        return str(self.errorInfo)+"年龄错误!"

#测试代码
if __name__=="__main__":
    age=int(input("输入一个年龄"))
    if age<1 or age>150:
        raise AgeError(age)
    else:
        print("正常的年龄 :",age)


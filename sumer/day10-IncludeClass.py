'''
#测试私有属性 __双下滑线打头
class Employer:
    #私有属性
    __complany="一个程序员"

    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def __work(self):
        print("好好工作")
        print(Employer.__complany)
e=Employer("陈章月",19)
#只能通过调类来调方法 下滑线_加类名加__双下滑线
print(e.name)
print(e._Employer__age)
print(dir(e))
e._Employer__work()
print(e._Employer__complany)

#@property装饰器 可以将一个方法调用变成"属性调用
#测试
'''


class Employee:

	def __init__(self, name, salary):
		self.__name = name
		self.__salary = salary

	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self, salary):
		if 100 < salary < 50000:
			self.__salary = salary
		else:
			print("录入错误")


'''
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 100<salary<50000:
            self.__salary=salary
        else:
            print("录入错误")
    @property
    def salary(self):
        print("salary run...")
        return 10000

emp1=Employee("陈章月",10000)
print(emp1.get_salary())
emp1.set_salary(20000)
print(emp1.get_salary())
emp1.salary=-2000
print(emp1.get_salary())
'''
emp1 = Employee("陈章月", 10000)
print(emp1.salary)
emp1.salary = -2000

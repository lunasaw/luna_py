# 测试继承

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say_age(self):
		print("年龄 我也不知道")

	def __str__(self):
		return "名字是{0}".format(self.name)


'''
class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age) #必须显试的调用父类构造方法,不如解释器不会去调用
        self.score=score
        #重写say_age方法
    def say_age(self):
        print("{0}的年龄是{1}".format(self.name,self.age))

print(Student.mro())
#Student->Person->OBject
s=Student("陈章月",19,59)
s.say_age()
#继承了私有属性 但是不能使用
#print(s.age)
#print(s._Person__age)
print(dir(s))
'''
# 测试重写__str__方法
p = Person("陈章月", 19)
print(p)

# py支持多重继承 java不支持  py的一个子类可以有多个父类 但会破坏类的整体层次 故不常用
# 特殊属性
print(Person.__bases__)
print(p.__str__())

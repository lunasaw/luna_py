class Singleton:
	_obj = None  # 类属性
	__init_flag = True

	def __new__(cls, *args, **kwargs):
		if cls._obj == None:
			cls._obj = object.__new__(cls)

		return cls._obj

	def __init__(self, name):
		if Singleton.__init_flag:
			print("init----")
			self.name = name
			Singleton.__init_flag = False


a = Singleton("aa")
b = Singleton("bb")  # 只创建一个类  顾名思义为单例
print(a)
print(a.name)
print(b)
print(b.name)

# 工厂和单例的结合使用
# 测试工程模式
class CreateFactory:
	_obj = None  # 类属性
	__init_flag = True

	def create_car(self, brand):
		if brand == "奔驰":
			return Benz()
		elif brand == "宝马":
			return BMW()
		elif brand == "比亚迪":
			return BYD()
		else:
			return "未知品牌"

	# 构造方法
	def __new__(cls, *args, **kwargs):
		if cls._obj == None:
			cls._obj = object.__new__(cls)

		return cls._obj

	def __init__(self):
		if CreateFactory.__init_flag:
			print("init--carfactory")

			CreateFactory.__init_flag = False


class Benz:
	pass


class BMW:
	pass


class BYD:
	pass


factory = CreateFactory()
factory1 = CreateFactory()
c1 = factory.create_car("奔驰")
c2 = factory1.create_car("比亚迪")
print(factory1)
print(factory)

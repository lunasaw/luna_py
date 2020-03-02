#测试工程模式
class CreateFactory:

    def create_car(self,brand):
        if brand=="奔驰":
            return Benz()
        elif brand=="宝马":
            return BMW()
        elif brand=="比亚迪":
            return BYD()
        else:
            return "未知品牌"

class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

factory =CreateFactory()
factory1=CreateFactory()
c1=factory.create_car("奔驰")
c2=factory1.create_car("比亚迪")
print(factory1)
print(factory)

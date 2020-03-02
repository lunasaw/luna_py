from distutils.core import setup
setup(
    name='supermethod', #对外我们模块的名字
    version='1.0',#版本号
    description='这是第一个对外发布的模块，测试哦',#描述
    # author='zychen',#作者
    author_email='Iszychen@gmail.com',
    py_modules=['supermethod.demo01-Files'] #要发布的模块
)
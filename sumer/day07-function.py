'''测试函数的定义
    名称必须符合标识符的规则
    def 名称():
        print()

    冒号内的为语句块 语句块的名字为标识符 通过名称调用语句块
    ()括号内为参数
    python中 万物皆对象
    定义后调用

def text01():
    str="我是一个函数"
    print(str)

# text01()
# for i in range(3):
#     text01()

print(id(text01()))
print(type(text01()))
print(text01())
text01()
'''
#带参数的函数
def printMax(a,b):
    '''用于比较两个数的大小,打印比较大的 并返回'''
    if a>b:
        print(a,'是较大值')
        return a
    else:
        print(b,'是较大值')
        return b


c=printMax(3,5)
print(c)
help(printMax.__doc__)
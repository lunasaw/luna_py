#异常练习 Traceback追踪溯源 most recent call last 最后一次调用
try:
    print("开始")
    a=1/0
    print("不会被输出")
#BaseException 所有异常父类
except BaseException as f:
    #f 是异常描述
    print("格式错误")
    print(f)
    print(type(f))
    '''
while True:
   try:
       x = int(input("请输入一个数字"))
       print("输入的数字:", x)
       if x == 99:
           print("退出")
           break
   except :#子类
       print("不能输入字母")
   #except: #父类
       
print("循环数字输入结束")
'''

try:
    a=input("请输入一个被除数")
    b=input("请输入一个除数")
    c=float(a)/float(b)
except ZeroDivisionError:
    print("异常:除数不能为0")
except ValueError:
    print("异常:不能将字符串转为数字")
except NameError:
    print("异常:变量不存在")
except BaseException as e:
    print(e)
#如果没有异常
else:
    print(c)
finally:
    print("无论发生什么我都会执行   通常用于关闭try中开启的资源")

try:
    f=open("b.txt")
    content=f.readline()
    print(content)
except:
    print("文件未找到")
finally:
    print("关闭资源")
    try:
        f.close()
    except:
        print("没有文件 关闭失败")

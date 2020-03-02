from builtins import enumerate

try:
    f = open("a.txt", "a")
    s = "it zychen 换行:\n 退格:\b 单引号:\' 双引号:\" 制表符:\t 反斜杠: \\ 回车:\r "  # "\n"
    f.write(s)
except BaseException as e:
    print(e)
finally: #必须执行
    f.close()

#with
with open(r"b.txt","a") as h:
    h.write("zychen i love you!")
#自动化管理  会回到打开前的操作

#文本文件的读取 参数可选的  read 默认开始到末尾  填多少表示读多少个字符
with open(r"b.txt","r") as k:
    print(k.read())

with open("b.txt","r") as j:
    for a in j:
        print(a)

with open("b.txt","r") as j:
    while True:
        fragment=j.readline()
        if not fragment:
            break
        else:
            print(fragment)

#每行增加行号
a=["陈章月","黎承红","列表"]
b=enumerate(a)
print(a)
print(list(b))
c=[temp+"#" +str(index)for index,temp in enumerate(a)]
print(c)

'''二进制文件
f=open(r"d:\a.txt","wb") #可写的、重写模式的二进制文件对象
f=open(r"d:\a.txt","ab")  #可写的、追加模式的二进制文件对象
f=open(r"d:\a.txt","rb") #可读的二进制文件对象
'''
with open("mygirl.gif","rb") as  f:
    with open("1_copy.gif" ,"wb") as  w:
        for line in  f.readlines():
            w.write(line)
print("图片拷贝完成!")
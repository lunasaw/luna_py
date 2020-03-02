# 负责拷贝压缩解压缩

'''
shutil.copyfile("mygirl.gif","1_copy.jpg")
#压缩 ->压缩后压缩包所在目录 压缩的格式 要压缩的内容
shutil.make_archive("","","")

#解压缩 压缩路径
z=zipfile.ZipFile("")
#放到哪个目录下
z.extract()
z.close()
'''


# 递归算法 自己掉自己
def a1():
    print("a1")


def b1():
    print("b1")


a1()


def function(n):
    if (n == 1):
        return 1
    return n * function(n - 1)


last = function(3)
print(last)

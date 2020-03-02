with open(r"a.txt", "r") as  f:
    print("文件名是 :{0}".format(f.name))
    print(f.tell())
    print("读取内容:{0}".format(str(f.readlines())))
    print(f.tell())
    print(f.tell())
    f.seek(0)
    print("读取的内容: {0}".format(str(f.readlines())))

# 序列化 pickle
import pickle

with open(r"d:\b.txt", "wb")  as  f:  # 二进制文件
    a1 = "陈章月"
    a2 = 18
    a3 = [19, 11, 70]

    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)

# 讲数据反序列化为对象
with open(r"d:\b.txt", "rb") as  f:
    a1 = pickle.load(f)
    a2 = pickle.load(f)
    a3 = pickle.load(f)
    print(a1)
    print(a2)
    print(a3)

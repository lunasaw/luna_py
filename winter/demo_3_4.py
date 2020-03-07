a = list(range(10))
print(id(a))
print("List生成列表\n", a)
c = a + ["qq"]
print("+连接生成新对象\n", c)
a.extend([9, 9])
print("extend 扩展 不生成新的对象 效率较高\n", c)
a.reverse()
print("reverse降序列表\n", a)
print("sort排序\n", a)
b = a.copy()
print("copy复制\n", b)
a.append(list(range(3)))
print(id(a))
print("append连接\n", a)
a.insert(2, [66])
print("insert往指定位置插入 原有的位置往后挪\n", a)
a.append(b)
a.remove(b)
print("remove移除指定数据\n", a)
x = a.pop(2)
print("pop删除指定位置的数据并返回值\n", a, "值为:", x)
del a[3]
print("删除 后面的往前挪 不反悔值 \n ", a)
print("判断数据有没有在列表里 常用 in\n", 9 in a)
print("判断数据有没有在列表里 count\n", a.count(9) > 0)

# 切片操作
print("提前整个列表 [:]\n ", a[:])
print("索引 [开始0:结束10:步长2 默认是1]\n ", a[:10:2])
print("索引负数 从右到左 [开始-10:结束-2:步长1 默认是1]\n ", a[-10:-2:2])

# 列表的遍历
print("列表的遍历")
for a in a:
	print(a)

import random

random.shuffle(b)
print("random.shuffle打乱列表\n", b)

print(id(b))
m = sorted(b)
print("sorted生成新对象\n", id(m), m)

# 迭代器 接受的是一个迭代器 通过list 函数转为列表
b.sort()
q = reversed(b)
print("迭代器反转\n", list(q))

# min 列表最小  max 列表最大  max 数字求和 其他报错

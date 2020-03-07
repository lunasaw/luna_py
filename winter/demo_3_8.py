# 集合 底层也是字典
a = {1, 2, 3, "chen"}
print(a)

# 复制
b = set(a)

# 增加
b.add("yue")

# 　删除
b.remove(2)
print(b)

# 数学操作
# 并集 union
print(a | b)
print(a.union(b))

# 交集 intersection
print(a & b)
print(a.intersection(b))

# 差集 -
print(a - b)

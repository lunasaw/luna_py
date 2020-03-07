# 字典 键值对
a = {'name': 'luna', 'age': 18}
b = dict(name='luna', age='18')
c = dict([("name", 'luna'), ("age", 18)])

# zip 创建
k = ['name', 'age']
v = ['luna', 18]
q = dict(zip(k, v))
print(q)

# fromkeys  创建空值初始化
e = dict.fromkeys(['name', 'age'])
print(e)

# 字典访问
print(a['name'])  # 键不存在 报异常 key error
print(a.get('name'))  # 键不存在返回none
# 可以指定不存在之后返回的值
print(a.get("hello", "不存在"))

# 列出所有的键值对
a.items()

# values 输出所有的值
print(a.values())

# keys 获取所有的键
print(a.keys())

# len 返回字典键值对数
print(len(a))

# 显示一个键是否在字典中  可用 in
print("hello" in a)

# 字典的添加=> 存在则覆盖  不存在 则添加
a["address"] = "重庆"
print(a.items())
a["name"] = "iszychen"
print(a.items())
print(a)

# 删除单个
del (a["address"])
print(a)

# pop 删除单个值并返回
pop = a.pop("name")
print(pop)
print(a)

# clear 清除所有
a.clear()
print(a)

# popitem 随机移除一个键值对 并返回 一个元组
m = b.popitem()
print(b)
print(m)

# 序列解包
x, y, z = (10, 20, 30)
print(x, y, z)

# 字典解包
c["address"] = "重庆"
q, w, e = c
print(q, w, e)
g, d, f = c.values()
print(g, d, f, )
h, i, j = c.items()
print(h, i, j)

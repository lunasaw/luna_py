#测试推导式
#列表推导式
y=[x*2 for x in range(1,50) if x%5==0]
print(y)

y=[]
for x in range(1,50):
    if x%5==0:
        y.append(x*2)
print(y)

cells = [(row, col) for row in range(1, 10) for col in range(1, 10)]
for cell in cells:
    print(cell)

#字典推导式
my_text = ' i love you, i love sxt, i love gaoqi'
char_count = {c:my_text.count(c)for c in my_text}
print(char_count)

#集合推导式  不可重复
v={x for x in range(1,100) if x%9==0}
print(v)

#生成器推导式
gnt=(x for x in range(4))
#print(tuple(gnt))
#print(tuple(gnt))

for x in  gnt : #gnt是一个可以迭代的对象 只能使用一次
    print(x,end=",")
print(tuple(gnt))

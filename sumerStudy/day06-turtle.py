import turtle

t=turtle.Pen()
t.width(4)
t.speed(1)
my_color =("red","green","yellow","black")
for i in range(100):
    t.penup()
    t.goto(0,-i*10)   #0, -10 ,-20,-30
    t.pendown()
    t.color(my_color[i%len(my_color)])
    t.circle(15+10*i)


#t.goto(0,0)
# t.circle(100)
#
# t.goto(0,-100)
# t.circle(200)
#
# t.goto(0,-200)
# t.circle(300)

turtle.done()  #程序执行完 窗口依然在
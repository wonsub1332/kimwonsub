import turtle

size=int(input("집의 크기 :"))
color=input("그리는 색 :")

t=turtle.Turtle()
t.color(color)
t.width(10)

t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)

t.rt(30)
t.fd(size)
t.rt(120)
t.fd(size)

input()
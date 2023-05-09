import turtle

t= turtle.Turtle("turtle")
t.shape("turtle")

s=turtle.textinput("","몇각형을 원하시나요?:")
n=int(s)
for i in range(n):
    t.fd(100)
    t.lt(360/n)
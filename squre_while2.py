import turtle

t= turtle.Turtle("turtle")
t.shape("turtle")

s=turtle.textinput("","몇각형을 원하시나요?:")
n=int(s)

i=0
while i < n:
    t.fd(100)
    t.lt(360/n)
    i=i+1
import turtle
t=turtle.Turtle()

t.shape("turtle")
t.color("green")
t.width(10)

size=200

t.fd(size)

t.up()
t.goto(0,size)
t.down()

t.fd(size)

input()
import turtle

window= turtle.Screen()
window.bgcolor("lightgreen")

t= turtle.Turtle()
t.shape("turtle")
t.width(3)

colors=["yellow","red","purple","blue"]
for c in colors:
    t.color(c)
    t.fd(200)
    t.lt(90)
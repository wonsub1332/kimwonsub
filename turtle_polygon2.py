import turtle

polygon = turtle.Turtle()

num_sides=int(input("사이드 개수를 입력하시오: "))
side_length=70
angle=360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
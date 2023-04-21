import turtle
turtle.bgcolor("black")

t = turtle.Turtle()

t.pensize(2)
t.speed(10)

colors = ["red", "purple", "white", "green", "blue", "magenta"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.fd(i)
    t.lt(59)

turtle.done()

import turtle

t = turtle.Turtle()
turtle.bgcolor("black")

t.pensize(2)
t.speed(10)

color = ["red", "green", "blue", "white", "purple", "yellow", "magenta"]
for i in range(42):
    t.color(color[i%7])
    t.circle(100)
    t.left(10)

turtle.done()

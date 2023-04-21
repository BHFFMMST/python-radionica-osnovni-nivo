import turtle
turtle.bgcolor("cyan")

t = turtle.Turtle()

t.fillcolor("white")
t.width(2)

n = int(input("Unesite broj uglova:"))

t.begin_fill()

for i in range(n):
    t.forward(100)
    t.left(360/n)

t.end_fill()

turtle.done()
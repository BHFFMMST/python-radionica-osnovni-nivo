import turtle

t = turtle.Turtle()

t.fillcolor("green")
t.width(5)

t.begin_fill()

for i in range(4):
    t.forward(150)
    t.right(90)

# povratak na koordinatni pocetak
t.home()

# crtamo drugi kvadrat koji je simetrican prvom
for i in range(4):
    t.backward(150)
    t.right(90)

t.end_fill()

turtle.done()
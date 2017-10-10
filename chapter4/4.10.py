import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Alex!")
tess = turtle.Turtle()
tess.color("pink")
tess.pensize(3)

for i in range(5):
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()
    for i in range(5):
        tess.forward(100)
        tess.right(144)
tess.hideturtle()

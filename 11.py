import turtle
wn = turtle.Screen()
wn.bgcolor("seashell")
wn.title("Hello, Alex!")
tess = turtle.Turtle()
tess.pensize(2)
for i in range(5):
    tess.forward(100)
    tess.right(145)
tess.hideturtle()
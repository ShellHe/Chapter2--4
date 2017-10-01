import turtle

def drawsquare(turt,size):
    for i in range(4):
        turt.fd(size)
        turt.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("turtles meet a function")

alex = turtle.Turtle()
wison = turtle.Turtle()
wison.color("seashell")
wison.setposition(-100,-100)
size = 100
for i in range(4):
    alex.forward(size)
    alex.left(90)

alli = turtle.Turtle()
alli.color("hotpink")
alli.penup()
alli.setpos(-100,-100)
drawsquare(wison,100)
drawsquare(alex, 200)

shell = turtle.Turtle()
shell.color("hotpink")
shell.penup()
shell.setpos(-100,-100)
shell.pendown

turts = [alex,shell.wison]
for i in turts: drasquare(1,100)
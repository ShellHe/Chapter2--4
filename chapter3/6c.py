import turtle
wn = turtle.Screen()
allie = turtle.Turtle()

sides = int(input("hwo many sides should I draw? "))
for i in range(sides):
    allie.forward(150)
    allie.left(360/sides)
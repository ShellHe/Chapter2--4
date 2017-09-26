import turtle
wn = turtle.Screen()
allie = turtle.Turtle()

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in turns:
    allie.left(i)
    allie.fd(100)
 
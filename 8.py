import turtle
wn = turtle.Screen()
allie = turtle.Turtle()

for xs in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    allie.forward(100)
    allie.left(xs)
print (allie.heading())
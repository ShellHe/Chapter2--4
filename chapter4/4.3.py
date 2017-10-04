import turtle
tess = turtle.Turtle()
def draw_poly(tess, sidenum, sz):
    for i in range(sidenum):
        tess.fd(sz)
        tess.lt(360/sidenum)
    tess.hideturtle()

draw_poly(tess, 8, 50)
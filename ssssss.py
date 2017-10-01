import turtle

def draw_squares(tess, size):
    for i in range(size):
        draw_multicolor_square(tess, size)
        size = size + 10
        tess.forward(10)
        tess.right(18)   
def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
#        t.color(i)
        t.forward(sz)
        t.right(90)
        wn = turtle.Screen()
        tess.pensize(3)

size = 20
tess = turtle.Turtle()
draw_squares(tess, size)
wn.mainloop()
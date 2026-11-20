import turtle


# Draw a square
def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


# Draw an isosceles triangle
def draw_trangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)


# Draw a rectangle with sides a and b
def draw_rectangle(lenght_a, lenght_b):
    for i in range(2):
        turtle.forward(lenght_a)
        turtle.right(90)
        turtle.forward(lenght_b)
        turtle.right(90)
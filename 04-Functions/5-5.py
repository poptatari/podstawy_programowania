import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

## Draw figures
# Two squares
pen.penup()
pen.goto(-250, 200)
pen.pendown()
figures.draw_square(80)

pen.penup()
pen.goto(100, 200)
pen.pendown()
figures.draw_square(110)

# Two triangles
pen.penup()
pen.goto(-250, 20)
pen.pendown()
figures.draw_trangle(90)

pen.penup()
pen.goto(100, -20)
pen.pendown()
figures.draw_trangle(120)

# Two rectangles
pen.penup()
pen.goto(-250, -100)
pen.pendown()
figures.draw_rectangle(120, 60)

pen.penup()
pen.goto(80, -90)
pen.pendown()
figures.draw_rectangle(150, 80)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
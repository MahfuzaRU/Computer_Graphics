import turtle
import time

#------------------Screen setup
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("2D translation")
turtle.tracer(0)

#------------Axes
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("gray")

#X axis
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

#Y axis
axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

#x label
axis.penup()
axis.goto(285, 15)
axis.write("X")

#x label
axis.penup()
axis.goto(10, 285)
axis.write("Y")

#drawing turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.pensize(2)

#original triangle
triangle = [(50, 50), (150, 50), (100, 150)]

#translation vector
tx = int(input("Enter Tx : "))
ty = int(input("Enter Ty : "))

#draw polygon
def draw(poly, color, show_points=False):
    t.penup()
    t.goto(poly[0])
    t.pendown()
    t.color(color)
    
    for p in poly[1 : ]:
        t.goto(p)
    t.goto(poly[0])
    
    if show_points:
        t.penup()
        
        for x, y in poly:
            t.goto(x+5, y+5)
            t.write(f"({x:.1f}, {y:.1f})", font=("Arial", 9, "normal"))

#animation
steps = 50

for i in range(steps + 1):
    t.clear()
    
    #original object
    draw(triangle, "gray", True)
    
    #current translated position
    dx = tx*i / steps
    dy = ty*i / steps
    
    moved = [(x+dx, y+dy) for x, y in triangle]
    
    #moving object
    draw(moved, "blue", True)
    
    turtle.update()
    time.sleep(0.03)
turtle.done()
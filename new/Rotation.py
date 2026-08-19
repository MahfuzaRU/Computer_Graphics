import turtle
import time
import math

#------------------Screen setup
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("2D Rotation")
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
#axis.penup()
axis.goto(10, 285)
axis.write("Y")

#drawing turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.pensize(2)

#original triangle
triangle = [(50, 50), (150, 50), (100, 150)]

#Rotation vector
angle = int(input("enter rotation angle : "))

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
    
#rotate polygon
def rotate(poly, theta):
    new = []
    r = math.radians(theta)
    
    for x, y in poly:
        xr = x*math.cos(r) - y*math.sin(r)
        yr = x*math.sin(r) - y*math.cos(r)
        new.append((xr, yr))
    return new


#animation
steps = 60

for i in range(steps + 1):
    t.clear()
    
    #original object
    draw(triangle, "gray", True)
    
    #current angle position
    current = angle*i / steps

    #rotated object
    rotated = rotate(triangle, current)
    draw(rotated, "blue", True)
    
    # Rotation point
    t.penup()
    t.goto(0, 0)
    t.dot(8, "red")
    
    turtle.update()
    time.sleep(0.03)
turtle.done()


'''
t.goto(x+5, y+5)

এর মানে:

x + 5 → point-এর 5 pixel ডানে
y + 5 → point-এর 5 pixel উপরে
Angle	কী হবে
0°	কোনো rotation হবে না
45°	45° ঘুরবে
90°	90° ঘুরবে — সবচেয়ে সহজে বোঝা যায়
180°	সম্পূর্ণ উল্টো দিকে যাবে
270°	270° ঘুরবে
360°	একবার পুরো ঘুরে আবার আগের অবস্থায় আসবে
'''

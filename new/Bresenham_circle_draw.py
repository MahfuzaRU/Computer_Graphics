import turtle
import time
import math

# ---------- Screen ----------
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("Bresenham Circle Drawing Algorithm")
turtle.tracer(0)

# ---------- Grid ----------
grid = turtle.Turtle()
grid.hideturtle()
grid.color("lightgray")

for i in range(-300, 301, 20):
    grid.penup()
    grid.goto(i, -300)
    grid.pendown()
    grid.goto(i, 300)

    grid.penup()
    grid.goto(-300, i)
    grid.pendown()
    grid.goto(300, i)

# ---------- Axes ----------
axis = turtle.Turtle()
axis.hideturtle()
axis.color("gray")

axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

axis.penup()
axis.goto(285, -15)
axis.write("X")

axis.goto(10, 285)
axis.write("Y")

# ---------- Origin ----------
axis.goto(0, 0)
axis.dot(8, "red")
axis.goto(8, 8)
axis.write("O (0,0)")

# ---------- Input ----------
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))

# ---------- Drawing Turtle ----------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ---------- Center Point ----------
t.goto(xc, yc)
t.dot(10, "red")
t.goto(xc + 8, yc + 8)
t.write(f"Center ({xc}, {yc})",
        font=("Arial", 10, "bold"))

# ---------- Radius Reference Point ----------
rx = xc + r
ry = yc

t.goto(rx, ry)
t.dot(10, "green")
t.goto(rx + 8, ry + 8)
t.write(f"R ({rx}, {ry})",
        font=("Arial", 10, "bold"))

# ---------- Reference Circle ----------
ref = turtle.Turtle()
ref.hideturtle()
ref.speed(0)
ref.color("lightgray")
ref.penup()

ref.goto(xc, yc - r)
ref.pendown()
ref.circle(r)

# ---------- Bresenham Circle ----------
x = 0
y = r
p = 3 - 2 * r

while x <= y:

    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]

    for px, py in points:
        t.goto(px, py)
        t.dot(6, "blue")

    turtle.update()
    time.sleep(0.04)

    if p < 0:
        p += 4 * x + 6
    else:
        p += 4 * (x - y) + 10
        y -= 1

    x += 1

# ---------- Show Reference Radius ----------
t.goto(xc, yc)
t.pendown()
t.goto(rx, ry)
t.penup()

turtle.update()
turtle.done()

'''
Enter center x: 0
Enter center y: 0
Enter radius: 100
'''

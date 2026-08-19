import turtle
import time

# ---------- Screen ----------
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("Midpoint Circle Drawing Algorithm")
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

# X-axis
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

# Y-axis
axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

# Axis labels
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
t.write(
    f"Center ({xc}, {yc})",
    font=("Arial", 10, "bold")
)

# ---------- Radius Reference Point ----------
rx = xc + r
ry = yc

t.goto(rx, ry)
t.dot(10, "green")
t.goto(rx + 8, ry + 8)
t.write(
    f"R ({rx}, {ry})",
    font=("Arial", 10, "bold")
)

# ---------- Reference Circle ----------
ref = turtle.Turtle()
ref.hideturtle()
ref.speed(0)
ref.color("lightgray")
ref.penup()

ref.goto(xc, yc - r)
ref.pendown()
ref.circle(r)

# ---------- Midpoint Circle Algorithm ----------
x = 0
y = r

# Initial decision parameter
p = 1 - r

while x <= y:

    # 8 symmetric points
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

    # Draw selected pixels
    for px, py in points:
        t.goto(px, py)
        t.dot(6, "blue")

    turtle.update()
    time.sleep(0.04)

    # Decision parameter update
    if p < 0:
        p = p + 2 * x + 3
    else:
        p = p + 2 * (x - y) + 5
        y -= 1

    x += 1

# ---------- Radius Line ----------
t.goto(xc, yc)
t.pendown()
t.goto(rx, ry)
t.penup()

turtle.update()
turtle.done()

'''
ধরি তুমি:

Center = (-4, 4)
Radius = 6

দিলে।

1. Initial values

Midpoint Circle Algorithm:

xc = -4
yc = 4
r  = 6

শুরু:

x=0
y=r=6

Decision parameter:

p=1-r

তাই:

p=1-6=-5

অর্থাৎ:

x = 0
y = 6
p = -5
2. প্রথম point

আমাদের local point:

(x,y) = (0,6)

Center যোগ করলে প্রথম actual point:
(xc + x, yc + y)
=(-4+0, 4+6)
=(-4,10)


example 2
xc = -4
yc = 6
r = 6
initial calculation
x=0
y=6
p=1-6=-5
first point:
(xc + x, yc + y)
=(-4 + 0, 6 + 6)
=(-4, 12)

short:
X = xc + x
Y = yc + y
ex 1:
Center (0,0) hole
X = x
Y = y
Center (-4,4) hole
X = x - 4
Y = y + 4
Center (-4,6) hole
X = x - 4
Y = y + 6

8- way symmetric mane jemon (x, y) = (2, 5)  একটা point থেকে symmetry ব্যবহার করে 8টা position পাওয়া যায়
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

'''

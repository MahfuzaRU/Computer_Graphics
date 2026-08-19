
import turtle
import time

# ---------- Screen ----------
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("Bresenham Line Drawing Algorithm")
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
#horizontal
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)
#vertical
axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

#axis label
axis.penup()
axis.goto(285, -15)
axis.write("X")
axis.goto(-285, -15)
axis.write("-X")
axis.goto(10, 285)
axis.write("Y")
axis.goto(10, -285)
axis.write("-Y")

# Origin
axis.goto(0, 0)
axis.dot(8, "red")
axis.goto(8, 8) #ai point a likha show korbe 
axis.write("O (0,0)")

# ---------- Input ----------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# ---------- Drawing Turtle ----------
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.pensize(2)
t.penup()

# Start & End points
for x, y, color, name in [
    (x1, y1, "red", "Start"),
    (x2, y2, "green", "End")
]:
    t.goto(x, y)
    t.dot(10, color)
    t.goto(x + 8, y + 8)
    t.write(f"{name} ({x}, {y})")

# ---------- Reference Line ----------
ref = turtle.Turtle()
ref.hideturtle()
ref.color("lightgray")
ref.penup()
ref.goto(x1, y1)
ref.pendown()
ref.goto(x2, y2)

# ---------- Bresenham ----------
dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

x, y = x1, y1

if dx >= dy:
    p = 2 * dy - dx
    end = x2

    while True:
        t.goto(x, y)
        t.dot(6, "blue")
        turtle.update()
        time.sleep(0.02)

        if x == end:
            break

        x += sx

        if p < 0:
            p += 2 * dy
        else:
            y += sy
            p += 2 * (dy - dx)

else:
    p = 2 * dx - dy
    end = y2

    while True:
        t.goto(x, y)
        t.dot(6, "blue")
        turtle.update()
        time.sleep(0.02)

        if y == end:
            break

        y += sy

        if p < 0:
            p += 2 * dx
        else:
            x += sx
            p += 2 * (dx - dy)

turtle.done()

'''
x1 = 50
y1 = 50
x2 = 200
y2 = 150

'''




'''


import turtle
import time

# ---------------- Screen ----------------
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("Bresenham Line Drawing Algorithm")
turtle.tracer(0)

def draw_grid():
    grid = turtle.Turtle()
    grid.hideturtle()
    grid.speed(0)
    grid.color("lightgray")

    # Vertical grid lines
    for x in range(-300, 301, 20):
        grid.penup()
        grid.goto(x, -300)
        grid.pendown()
        grid.goto(x, 300)

    # Horizontal grid lines
    for y in range(-300, 301, 20):
        grid.penup()
        grid.goto(-300, y)
        grid.pendown()
        grid.goto(300, y)

draw_grid()

# ---------------- Axes ----------------
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
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

axis.penup()
axis.goto(285, -15)
axis.write("X")
axis.goto(10, 285)
axis.write("Y")

# Origin (0,0)
axis.goto(0, 0)
axis.dot(8, "red")
axis.goto(8, 8)
axis.write("O (0,0)", font=("Arial", 10, "normal"))

# ---------------- Drawing Turtle ----------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ---------------- Input ----------------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# ---------------- Show Start and End Points ----------------

# Start point
t.penup()
t.goto(x1, y1)
t.dot(10, "red")
t.goto(x1 + 8, y1 + 8)
t.write(f"Start ({x1}, {y1})", font=("Arial", 10, "bold"))

# End point
t.goto(x2, y2)
t.dot(10, "green")
t.goto(x2 + 8, y2 + 8)
t.write(f"End ({x2}, {y2})", font=("Arial", 10, "bold"))

# Reference (ideal) line
ref = turtle.Turtle()
ref.hideturtle()
ref.speed(0)
ref.color("lightgray")
ref.penup()
ref.goto(x1, y1)
ref.pendown()
ref.goto(x2, y2)

# ---------------- Bresenham Algorithm ----------------
dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

x, y = x1, y1

if dx >= dy:
    p = 2 * dy - dx

    while True:
        t.goto(x, y)
        t.dot(6, "blue")
        turtle.update()
        time.sleep(0.02)

        if x == x2:
            break

        x += sx

        if p < 0:
            p += 2 * dy
        else:
            y += sy
            p += 2 * (dy - dx)

else:
    p = 2 * dx - dy

    while True:
        t.goto(x, y)
        t.dot(6, "blue")
        turtle.update()
        time.sleep(0.02)

        if y == y2:
            break

        y += sy

        if p < 0:
            p += 2 * dx
        else:
            x += sx
            p += 2 * (dx - dy)

 
turtle.done()

'''

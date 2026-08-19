import turtle
import time

# ---------- Screen ----------
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("DDA Line Drawing Algorithm")
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

axis.goto(-285, -15)
axis.write("-X")

axis.goto(10, -285)
axis.write("-Y")

# ---------- Origin ----------
axis.goto(0, 0)
axis.dot(8, "red")
axis.goto(8, 8)
axis.write("O (0,0)")

# ---------- Input ----------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# ---------- Drawing Turtle ----------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ---------- Start Point ----------
t.goto(x1, y1)
t.dot(10, "red")
t.goto(x1 + 8, y1 + 8)
t.write(
    f"Start ({x1}, {y1})",
    font=("Arial", 10, "bold")
)

# ---------- End Point ----------
t.goto(x2, y2)
t.dot(10, "green")
t.goto(x2 + 8, y2 + 8)
t.write(
    f"End ({x2}, {y2})",
    font=("Arial", 10, "bold")
)

# ---------- Reference Line ----------
ref = turtle.Turtle()
ref.hideturtle()
ref.speed(0)
ref.color("lightgray")

ref.penup()
ref.goto(x1, y1)
ref.pendown()
ref.goto(x2, y2)

# ---------- DDA Algorithm ----------

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

for i in range(steps + 1):

    # Plot current pixel
    t.goto(round(x), round(y))
    t.dot(6, "blue")

    turtle.update()
    time.sleep(0.03)

    # Calculate next point
    x += x_inc
    y += y_inc

turtle.done()
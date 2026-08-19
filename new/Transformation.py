import turtle
import math
import time

# ---------- Screen ----------
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("2D Geometric Transformations")
turtle.tracer(0)

# ---------- Axes ----------
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("gray")

axis.penup(); axis.goto(-300, 0)
axis.pendown(); axis.goto(300, 0)

axis.penup(); axis.goto(0, -300)
axis.pendown(); axis.goto(0, 300)

axis.penup(); axis.goto(285, -15)
axis.write("X")
axis.goto(10, 285)
axis.write("Y")

# ---------- Drawing Turtle ----------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

triangle = [(50,50), (150,50), (100,150)]

def draw(poly, color):
    t.penup()
    t.goto(poly[0])
    t.pendown()
    t.color(color)

    for p in poly[1:]:
        t.goto(p)

    t.goto(poly[0])

# ---------- Translation ----------
def translation(tx, ty):
    steps = 60

    for i in range(steps+1):
        t.clear()
        draw(triangle, "gray")

        dx = tx*i/steps
        dy = ty*i/steps

        moved = [(x+dx, y+dy) for x,y in triangle]
        draw(moved, "blue")

        turtle.update()
        time.sleep(0.03)

# ---------- Rotation ----------
def rotation(angle):
    steps = 60

    for i in range(steps+1):
        t.clear()
        draw(triangle, "gray")

        th = math.radians(angle*i/steps)

        rot = []
        for x,y in triangle:
            xr = x*math.cos(th) - y*math.sin(th)
            yr = x*math.sin(th) + y*math.cos(th)
            rot.append((xr,yr))

        draw(rot, "blue")

        t.penup()
        t.goto(0,0)
        t.dot(8,"red")

        turtle.update()
        time.sleep(0.03)

# ---------- Scaling ----------
def scaling(sx, sy):
    steps = 60

    for i in range(steps+1):
        t.clear()
        draw(triangle, "gray")

        fx = 1 + (sx-1)*i/steps
        fy = 1 + (sy-1)*i/steps

        scale = [(x*fx, y*fy) for x,y in triangle]
        draw(scale, "blue")

        turtle.update()
        time.sleep(0.03)

# ---------- Menu ----------
print("1. Translation")
print("2. Rotation")
print("3. Scaling")

choice = int(input("Enter choice: "))

if choice == 1:
    tx = int(input("Enter Tx: "))
    ty = int(input("Enter Ty: "))
    translation(tx, ty)

elif choice == 2:
    angle = int(input("Enter Angle: "))
    rotation(angle)

elif choice == 3:
    sx = float(input("Enter Sx: "))
    sy = float(input("Enter Sy: "))
    scaling(sx, sy)

turtle.done()
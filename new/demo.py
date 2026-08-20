import turtle
import time
import math

#------------------Screen setup
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("2D translation")
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

#------------Axes
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("black")

#X axis horizontal
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

#Y axis vertical
axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)


# ---------- Axis Labels ----------
axis.penup()

axis.goto(285, -15)
axis.write("+X")

axis.goto(-300, -15)
axis.write("-X")

axis.goto(8, 235)
axis.write("+Y")

axis.goto(8, -250)
axis.write("-Y")

# ---------- Origin ----------
axis.goto(0, 0)
axis.dot(8, "red")
axis.goto(8, 8)
axis.write("O (0,0)")

#drawing turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(3)
t.pensize(2)

#original triangle
triangle = [(50, 50), (150, 50), (100, 150)]

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



# ---------- Translation ----------
def translation(tx, ty):
    steps = 60

    for i in range(steps+1):
        t.clear()
        draw(triangle, "gray", True)

        dx = tx*i/steps
        dy = ty*i/steps

        moved = [(x+dx, y+dy) for x,y in triangle]
        draw(moved, "blue", True)

        turtle.update()
        time.sleep(0.03)

# ---------- Rotation ----------
def rotation(angle):
    steps = 60

    for i in range(steps+1):
        t.clear()
        draw(triangle, "gray", True)

        th = math.radians(angle*i/steps)

        rot = []
        for x,y in triangle:
            xr = x*math.cos(th) - y*math.sin(th)
            yr = x*math.sin(th) + y*math.cos(th)
            rot.append((xr,yr))

        draw(rot, "blue", True)

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
        draw(triangle, "gray", True)

        fx = 1 + (sx-1)*i/steps
        fy = 1 + (sy-1)*i/steps

        scale = [(x*fx, y*fy) for x,y in triangle]
        draw(scale, "blue", True)

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
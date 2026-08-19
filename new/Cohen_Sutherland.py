import turtle
import time
# ---------- Screen ----------
screen = turtle.Screen()
screen.setup(700, 600)
screen.title("Cohen-Sutherland Line Clipping")

axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("gray")

# X-axis
axis.penup(); axis.goto(-300, 0)
axis.pendown(); axis.goto(300, 0)

# Y-axis
axis.penup(); axis.goto(0, -250)
axis.pendown(); axis.goto(0, 250)

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

# ---------- Clipping Window ----------
xmin, ymin = -100, -50
xmax, ymax = 100, 80

# ---------- Input ----------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

ox1, oy1 = x1, y1
ox2, oy2 = x2, y2



# Window
w = turtle.Turtle()
w.hideturtle()
w.speed(0)
w.pensize(2)

w.penup(); w.goto(xmin, ymin)
w.pendown()
for _ in range(2):
    w.forward(xmax-xmin)
    w.left(90)
    w.forward(ymax-ymin)
    w.left(90)

# Original line
o = turtle.Turtle()
o.hideturtle()
o.speed(0)
o.color("gray")
o.pensize(2)

o.penup()
o.goto(ox1, oy1)
o.pendown()
o.goto(ox2, oy2)


# ---------- Original Start Point ----------
o.penup()
o.goto(ox1, oy1)
o.dot(10, "red")
o.goto(ox1 + 8, oy1 + 8)
o.write(
    f"Start ({ox1},{oy1})",
    font=("Arial", 9, "bold")
)

# ---------- Original End Point ----------
o.goto(ox2, oy2)
o.dot(10, "green")
o.goto(ox2 + 8, oy2 + 8)
o.write(
    f"End ({ox2},{oy2})",
    font=("Arial", 9, "bold")
)

# ---------- Cohen-Sutherland ----------
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def code(x, y):
    c = INSIDE
    if x < xmin: c |= LEFT
    elif x > xmax: c |= RIGHT
    if y < ymin: c |= BOTTOM
    elif y > ymax: c |= TOP
    return c

c1 = code(x1, y1)
c2 = code(x2, y2)

accept = False

while True:

    if c1 == 0 and c2 == 0:
        accept = True
        break

    if c1 & c2:
        break

    out = c1 if c1 else c2

    if out & TOP:
        x = x1 + (x2-x1)*(ymax-y1)/(y2-y1)
        y = ymax

    elif out & BOTTOM:
        x = x1 + (x2-x1)*(ymin-y1)/(y2-y1)
        y = ymin

    elif out & RIGHT:
        y = y1 + (y2-y1)*(xmax-x1)/(x2-x1)
        x = xmax

    else:
        y = y1 + (y2-y1)*(xmin-x1)/(x2-x1)
        x = xmin

    if out == c1:
        x1, y1 = x, y
        c1 = code(x1, y1)
    else:
        x2, y2 = x, y
        c2 = code(x2, y2)

# ---------- Animation ----------
time.sleep(1)

if accept:
    clip = turtle.Turtle()
    clip.hideturtle()
    clip.speed(0)
    clip.color("blue")
    clip.pensize(4)

    clip.penup()
    clip.goto(x1, y1)
    clip.pendown()

    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x = x1
    y = y1

    for i in range(steps):
        clip.goto(x, y)
        x += dx / steps
        y += dy / steps
        time.sleep(0.01)

    clip.goto(x2, y2)

    print("Accepted")
    print(f"Clipped Line: ({x1:.2f}, {y1:.2f}) → ({x2:.2f}, {y2:.2f})")

else:
    print("Line Rejected")

turtle.done()

'''
Enter x1: -200
Enter y1: -100
Enter x2: 200
Enter y2: 150
Accepted
Clipped Line: (-100.00, -37.50) → (88.00, 80.00)


'''
import turtle
import time

# ---------- Screen ----------
screen = turtle.Screen()
screen.setup(1000, 800)
screen.title("Koch Snowflake - Deterministic Self-Similar Fractal")

turtle.tracer(0)

# ---------- Depth Display Turtle ----------
info = turtle.Turtle()
info.hideturtle()
info.penup()
info.goto(0, 330)

# ---------- Drawing Turtle ----------
t = turtle.Turtle()
t.speed(0)
t.pensize(3)


# ---------- Koch Curve ----------
def koch_curve(t, length, depth):

    if depth == 0:
        t.forward(length)
        turtle.update()
        time.sleep(0.01)
        return

    length = length / 3

    koch_curve(t, length, depth - 1)

    t.left(60)

    koch_curve(t, length, depth - 1)

    t.right(120)

    koch_curve(t, length, depth - 1)

    t.left(60)

    koch_curve(t, length, depth - 1)


# ---------- Snowflake ----------
def snowflake(t, length, depth):

    for i in range(3):
        koch_curve(t, length, depth)
        t.right(120)


# ---------- Show Depth 0 to 3 ----------
for depth in range(5):

    t.clear()
    info.clear()

    # Show current depth
    info.write(
        f"Koch Snowflake - Depth = {depth}",
        align="center",
        font=("Arial", 24, "bold")
    )

    # Starting position
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()


    # Color
    colors = ["purple", "red", "green", "blue", "orange"]
    t.pencolor(colors[depth])


    # Draw
    snowflake(t, 300, depth)

    turtle.update()

    time.sleep(2)


screen.exitonclick()
import matplotlib.pyplot as plt
import math

# Original triangle
x = [2, 4, 3, 2]
y = [2, 2, 5, 2]


# ---------------- TRANSLATION ----------------
def translation(x, y, tx, ty):
    x_new = [i + tx for i in x]
    y_new = [i + ty for i in y]
    return x_new, y_new


# ---------------- ROTATION ----------------
def rotation(x, y, angle):
    theta = math.radians(angle)

    x_new = [
        i * math.cos(theta) - j * math.sin(theta)
        for i, j in zip(x, y)
    ]

    y_new = [
        i * math.sin(theta) + j * math.cos(theta)
        for i, j in zip(x, y)
    ]

    return x_new, y_new


# ---------------- SCALING ----------------
def scaling(x, y, sx, sy):
    x_new = [i * sx for i in x]
    y_new = [i * sy for i in y]
    return x_new, y_new


# Apply transformations
xt, yt = translation(x, y, 5, 2)
xr, yr = rotation(x, y, 45)
xs, ys = scaling(x, y, 2, 1.5)


# ---------------- DRAW ----------------

# Original
plt.plot(x, y, '--', label="Original")

# Translation
plt.plot(xt, yt, linewidth=3, label="Translation")

# Rotation
plt.plot(xr, yr, linewidth=3, label="Rotation")

# Scaling
plt.plot(xs, ys, linewidth=3, label="Scaling")

# Original points
plt.scatter(x[:-1], y[:-1])

# Origin / rotation point
plt.scatter(0, 0, s=60, label="Rotation Point")

plt.title("2D Geometric Transformations")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
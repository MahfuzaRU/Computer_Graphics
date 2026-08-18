

import matplotlib.pyplot as plt
import math

# Four control points
P0 = (1, 1)
P1 = (2, 6)
P2 = (7, 6)
P3 = (8, 1)

X = []
Y = []

# Generate Bezier curve
for i in range(101):
    t = i / 100

    x = ((1-t)**3 * P0[0] +
         3*(1-t)**2*t * P1[0] +
         3*(1-t)*t**2 * P2[0] +
         t**3 * P3[0])

    y = ((1-t)**3 * P0[1] +
         3*(1-t)**2*t * P1[1] +
         3*(1-t)*t**2 * P2[1] +
         t**3 * P3[1])

    X.append(x)
    Y.append(y)

# Control polygon
px = [P0[0], P1[0], P2[0], P3[0]]
py = [P0[1], P1[1], P2[1], P3[1]]

plt.plot(px, py, '--', label="Control Polygon")
plt.scatter(px, py, s=50, label="Control Points")

# Bezier curve
plt.plot(X, Y, linewidth=3, label="Bezier Curve")

plt.title("Cubic Bezier Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()
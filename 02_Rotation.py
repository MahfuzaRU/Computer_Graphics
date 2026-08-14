import matplotlib.pyplot as plt
import math

# Triangle vertices
x = [2, 4, 3, 2]
y = [2, 2, 5, 2]

# Rotation angle
angle = 45
theta = math.radians(angle)

# Rotation about origin
x_new = [i * math.cos(theta) - j * math.sin(theta) for i, j in zip(x, y)]
y_new = [i * math.sin(theta) + j * math.cos(theta) for i, j in zip(x, y)]

# Original object
plt.plot(x, y, '--', label="Original")

# Rotated object
plt.plot(x_new, y_new, linewidth=3, label="Rotated")

# Vertices
plt.scatter(x, y)
plt.scatter(x_new, y_new)

# Origin
plt.scatter(0, 0, s=80, label="Origin")

plt.title("2D Rotation")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()

'''
Rotation turns an object by a specified angle around a fixed point. For rotation about the origin, the new coordinates are: x' = x cos(theta) - y sin(theta) y' = x sin(theta) + y cos(theta)

'''

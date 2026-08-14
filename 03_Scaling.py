import matplotlib.pyplot as plt

# Triangle vertices
x = [2, 4, 3, 2]
y = [2, 2, 5, 2]

# Scaling factors
sx, sy = 2, 1.5

# Scaled coordinates
x_new = [i * sx for i in x]
y_new = [i * sy for i in y]

# Original object
plt.plot(x, y, '--', label="Original")

# Scaled object
plt.plot(x_new, y_new, linewidth=3, label="Scaled")

# Vertices
plt.scatter(x, y)
plt.scatter(x_new, y_new)

plt.title("2D Scaling")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()


'''
Scaling changes the size of an object. If sx and sy are the horizontal 
and vertical scaling factors, then: x' = sx * x y' = sy * y A factor greater 
than 1 enlarges the object, while a factor between 0 and 1 shrinks it.

'''

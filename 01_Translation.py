

import matplotlib.pyplot as plt

# Triangle vertices
x = [2, 4, 3, 2]
y = [2, 2, 5, 2]

# Translation values
tx, ty = 4, 3

# Translated coordinates
x_new = [i + tx for i in x]
y_new = [i + ty for i in y]

# Original object
plt.plot(x, y, '--', label="Original")

# Translated object
plt.plot(x_new, y_new, linewidth=3, label="Translated")

# Show vertices
plt.scatter(x, y)
plt.scatter(x_new, y_new)

plt.title("2D Translation")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()

'''
Translation moves an object from one position to another without changing its shape, size, or orientation. If a point is (x, y) and the translation values are (tx, ty), then the new point is (x + tx, y + ty).

'''

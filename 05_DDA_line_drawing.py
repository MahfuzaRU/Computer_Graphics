import matplotlib.pyplot as plt

# Take input from keyboard
x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

# Calculate differences
dx = x2 - x1
dy = y2 - y1

# Calculate number of steps
steps = max(abs(dx), abs(dy))

# Calculate increment values
x_inc = dx / steps
y_inc = dy / steps

# Starting point
x = x1
y = y1

# Store generated pixels
X = []
Y = []

# DDA Line Drawing Algorithm
for i in range(steps + 1):

    X.append(round(x))
    Y.append(round(y))

    x += x_inc
    y += y_inc

# Print generated pixel coordinates
print("\nDDA Pixel Coordinates:")

for i in range(len(X)):
    print(f"({X[i]}, {Y[i]})")

# Draw DDA pixels
plt.scatter(
    X,
    Y,
    s=60,
    color="blue",
    label="DDA Pixels"
)

# Draw ideal/direct line
plt.plot(
    [x1, x2],
    [y1, y2],
    linestyle="--",
    color="red",
    linewidth=1,
    label="Direct Line"
)

# Connect generated pixels
plt.plot(
    X,
    Y,
    linestyle="-",
    color="gray",
    linewidth=0.8
)

# Graph settings
plt.xlabel("X")
plt.ylabel("Y")
plt.title("DDA Line Drawing Algorithm")
plt.grid(True)
plt.legend()
plt.axis("equal")

# Show graph
plt.show()
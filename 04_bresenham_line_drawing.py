import matplotlib.pyplot as plt

# Take input from keyboard
x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

# Calculate differences
dx = abs(x2 - x1)
dy = abs(y2 - y1)

# Determine direction
sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

# Starting point
x = x1
y = y1

# Store generated pixels
X = []
Y = []

# Bresenham Line Drawing Algorithm
if dx > dy:
    p = 2 * dy - dx

    while True:
        X.append(x)
        Y.append(y)

        if x == x2:
            break

        x += sx

        if p < 0:
            p += 2 * dy
        else:
            y += sy
            p += 2 * dy - 2 * dx

else:
    p = 2 * dx - dy

    while True:
        X.append(x)
        Y.append(y)

        if y == y2:
            break

        y += sy

        if p < 0:
            p += 2 * dx
        else:
            x += sx
            p += 2 * dx - 2 * dy

# Print generated pixel coordinates
print("\nBresenham Pixel Coordinates:")
for i in range(len(X)):
    print(f"({X[i]}, {Y[i]})")

# Draw Bresenham pixels
plt.scatter(X, Y, s=60, color="blue", label="Bresenham Pixels")

# Draw direct line
plt.plot(
    [x1, x2],
    [y1, y2],
    color="red",
    linewidth=1,
    label="Direct Line"
)

# Connect generated pixels
plt.plot(
    X,
    Y,
    linestyle="--",
    color="gray",
    linewidth=0.8
)

# Graph settings
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.legend()
plt.axis("equal")

# Show graph
plt.show()

'''
#solve 1
import matplotlib.pyplot as plt

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

x, y = x1, y1

X = []
Y = []

if dx > dy:
    p = 2 * dy - dx

    while True:
        X.append(x)
        Y.append(y)

        if x == x2:
            break

        x += sx

        if p < 0:
            p += 2 * dy
        else:
            y += sy
            p += 2 * dy - 2 * dx

else:
    p = 2 * dx - dy

    while True:
        X.append(x)
        Y.append(y)

        if y == y2:
            break

        y += sy

        if p < 0:
            p += 2 * dx
        else:
            x += sx
            p += 2 * dx - 2 * dy

# Draw the Bresenham pixels
plt.scatter(X, Y, s=50, color='blue', label='Bresenham Pixels')

# Direct line connecting the two endpoints
plt.plot([x1, x2], [y1, y2], linewidth=1, label='Direct Line')

# Connect pixels so the line is clearly visible
plt.plot(X, Y, linestyle='--', color='gray', linewidth=0.5)



plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.axis("equal")
plt.show()

'''



'''
#solve2
import matplotlib.pyplot as plt

# Sample endpoints
x1, y1 = 2, 3
x2, y2 = 12, 9

def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    return points

points = bresenham(x1, y1, x2, y2)

x = [p[0] for p in points]
y = [p[1] for p in points]

print("Generated pixels:", points)

plt.plot(x, y, marker="s")
plt.title("Bresenham Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()

'''

'''

Input:
Enter x1 y1: 2 3
Enter x2 y2: 10 8
Output:
Bresenham Pixel Coordinates:
(2, 3)
(3, 4)
(4, 4)
(5, 5)
(6, 6)
(7, 6)
(8, 7)
(9, 7)
(10, 8)

কয়টা pixel point পাওয়া যাবে সেটা input point দুটির উপর নির্ভর করে।

Bresenham Line Drawing Algorithm-এ মোট pixel সংখ্যা নির্ভর করে:

Line-এর length (distance)
dx = |x2 - x1|
dy = |y2 - y1|
Line কোন direction-এ যাচ্ছে (slope)

Condition	        Point সংখ্যা
dx > dy	            dx + 1
dy > dx	            dy + 1
dx = dy (45° line)	dx + 1

অর্থাৎ, যে axis বরাবর বেশি movement হয়, সেই axis-এর difference + 1 হবে মোট pixel সংখ্যা।

'''
import matplotlib.pyplot as plt
import math

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    X, Y = [], []

    while x <= y:

        pts = [
            (xc+x, yc+y), (xc-x, yc+y),
            (xc+x, yc-y), (xc-x, yc-y),
            (xc+y, yc+x), (xc-y, yc+x),
            (xc+y, yc-x), (xc-y, yc-x)
        ]

        for px, py in pts:
            X.append(px)
            Y.append(py)

        if d < 0:
            d = d + 4*x + 6
        else:
            d = d + 4*(x-y) + 10
            y -= 1

        x += 1

    return X, Y


xc, yc = map(int, input("Center: ").split())
r = int(input("Radius: "))

X, Y = bresenham_circle(xc, yc, r)

plt.scatter(X, Y, s=35, label="Bresenham Pixels")

theta = [i*math.pi/180 for i in range(361)]
plt.plot([xc+r*math.cos(t) for t in theta],
         [yc+r*math.sin(t) for t in theta],
         '--', color='gray', label="Ideal Circle")

plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
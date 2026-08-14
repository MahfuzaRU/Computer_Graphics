

import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 2, 2
xmax, ymax = 8, 7

# Polygon vertices
polygon = [(1, 3), (5, 9), (10, 6), (7, 1), (3, 1)]


def inside(p, edge):
    x, y = p

    if edge == "left":
        return x >= xmin
    if edge == "right":
        return x <= xmax
    if edge == "bottom":
        return y >= ymin
    if edge == "top":
        return y <= ymax


def intersection(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    if edge == "left":
        x = xmin
        y = y1 + (y2-y1) * (xmin-x1) / (x2-x1)

    elif edge == "right":
        x = xmax
        y = y1 + (y2-y1) * (xmax-x1) / (x2-x1)

    elif edge == "bottom":
        y = ymin
        x = x1 + (x2-x1) * (ymin-y1) / (y2-y1)

    elif edge == "top":
        y = ymax
        x = x1 + (x2-x1) * (ymax-y1) / (y2-y1)

    return (x, y)


def clip_polygon(poly, edge):
    result = []

    for i in range(len(poly)):
        current = poly[i]
        previous = poly[i-1]

        curr_in = inside(current, edge)
        prev_in = inside(previous, edge)

        if curr_in:
            if not prev_in:
                result.append(intersection(previous, current, edge))
            result.append(current)

        elif prev_in:
            result.append(intersection(previous, current, edge))

    return result


# Clip against all four boundaries
clipped = polygon

for edge in ["left", "right", "bottom", "top"]:
    clipped = clip_polygon(clipped, edge)


# ---------------- DRAW ----------------

# Close original polygon
original = polygon + [polygon[0]]
ox, oy = zip(*original)

# Close clipped polygon
clipped_closed = clipped + [clipped[0]]
cx, cy = zip(*clipped_closed)

# Clipping window
wx = [xmin, xmax, xmax, xmin, xmin]
wy = [ymin, ymin, ymax, ymax, ymin]

# Original polygon
plt.plot(ox, oy, '--', label="Original Polygon")

# Clipping window
plt.plot(wx, wy, linewidth=2, label="Clipping Window")

# Clipped polygon
plt.plot(cx, cy, linewidth=3, label="Clipped Polygon")

# Vertices
plt.scatter(ox, oy)
plt.scatter(cx, cy)

plt.title("Sutherland-Hodgman Polygon Clipping")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()

print("Clipped Polygon:")
for p in clipped:
    print(tuple(round(v, 2) for v in p))


import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 50, 50
xmax, ymax = 250, 200

# Take line input
x1, y1 = map(float, input("Enter x1 y1: ").split())
x2, y2 = map(float, input("Enter x2 y2: ").split())

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


# Find region code of a point
def get_code(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


# Save original line
ox1, oy1 = x1, y1
ox2, oy2 = x2, y2

# Get initial region codes
code1 = get_code(x1, y1)
code2 = get_code(x2, y2)

accept = False


# Cohen-Sutherland Line Clipping Algorithm
while True:

    # Completely inside
    if code1 == 0 and code2 == 0:
        accept = True
        break

    # Completely outside
    elif code1 & code2:
        break

    # Partially inside
    else:

        # Select outside point
        if code1 != 0:
            code_out = code1
        else:
            code_out = code2

        # Find intersection point

        # TOP
        if code_out & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax

        # BOTTOM
        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin

        # RIGHT
        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax

        # LEFT
        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        # Update outside endpoint
        if code_out == code1:
            x1, y1 = x, y
            code1 = get_code(x1, y1)

        else:
            x2, y2 = x, y
            code2 = get_code(x2, y2)


# Print result
if accept:
    print("\nLine Accepted")
    print(f"Clipped Line: ({x1:.2f}, {y1:.2f}) -> ({x2:.2f}, {y2:.2f})")

else:
    print("\nLine Completely Rejected")


# ---------------- GRAPH ----------------

# Original line
plt.plot(
    [ox1, ox2],
    [oy1, oy2],
    linestyle="--",
    color="gray",
    linewidth=1.5,
    label="Original Line"
)

# Clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    linewidth=2,
    label="Clipping Window"
)

# Original endpoints
plt.scatter(
    [ox1, ox2],
    [oy1, oy2],
    s=60,
    label="Original Endpoints"
)

# Clipped line
if accept:

    plt.plot(
        [x1, x2],
        [y1, y2],
        linewidth=4,
        label="Clipped Line"
    )

    # Clipped endpoints
    plt.scatter(
        [x1, x2],
        [y1, y2],
        s=70,
        marker="x",
        label="Clipped Endpoints"
    )


# Graph settings
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cohen-Sutherland Line Clipping Algorithm")

plt.grid(True)
plt.legend()
plt.axis("equal")

plt.show()

'''

import matplotlib.pyplot as plt

# Clipping window
xmin, ymin = 50, 50
xmax, ymax = 250, 200

# Input line
x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def get_code(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code


# Save original coordinates
ox1, oy1 = x1, y1
ox2, oy2 = x2, y2

code1 = get_code(x1, y1)
code2 = get_code(x2, y2)

accept = False

while True:

    # Completely inside
    if code1 == 0 and code2 == 0:
        accept = True
        break

    # Completely outside
    elif code1 & code2:
        break

    else:
        if code1 != 0:
            code_out = code1
        else:
            code_out = code2

        if code_out & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax

        elif code_out & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin

        elif code_out & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax

        elif code_out & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        if code_out == code1:
            x1, y1 = x, y
            code1 = get_code(x1, y1)
        else:
            x2, y2 = x, y
            code2 = get_code(x2, y2)


# ---------------- GRAPH ----------------

plt.figure(figsize=(8, 6))

# 1. Original complete line
plt.plot(
    [ox1, ox2], [oy1, oy2],
    '--',
    color='gray',
    linewidth=1.5,
    label='Original Line'
)

# 2. Clipping window
plt.plot(
    [xmin, xmax, xmax, xmin, xmin],
    [ymin, ymin, ymax, ymax, ymin],
    linewidth=2,
    label='Clipping Window'
)

# 3. Original endpoints
plt.scatter(
    [ox1, ox2], [oy1, oy2],
    s=60,
    label='Original Endpoints'
)

# 4. Clipped portion
if accept:
    plt.plot(
        [x1, x2], [y1, y2],
        linewidth=4,
        label='Clipped Line'
    )

    # Clipped endpoints
    plt.scatter(
        [x1, x2], [y1, y2],
        s=70,
        marker='x',
        label='Clipped Endpoints'
    )

    print("\nLine Accepted")
    print(f"Clipped line: ({x1:.2f}, {y1:.2f}) -> ({x2:.2f}, {y2:.2f})")

else:
    print("\nLine Completely Rejected")


# Labels
plt.text(ox1, oy1, f"  P1({ox1},{oy1})")
plt.text(ox2, oy2, f"  P2({ox2},{oy2})")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cohen-Sutherland Line Clipping Algorithm")

plt.legend()
plt.grid(True)
plt.axis("equal")

# Add some space around the window
plt.xlim(min(ox1, xmin) - 30, max(ox2, xmax) + 30)
plt.ylim(min(oy1, ymin) - 30, max(oy2, ymax) + 30)

plt.show()

'''
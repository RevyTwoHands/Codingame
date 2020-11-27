import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

xMax = w - 1
xMin = 0
yMax = h - 1
yMin = 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if 'R' in bomb_dir:
        xMin = x0 + 1

    elif 'L' in bomb_dir:
        xMax = x0 - 1

    if 'D' in bomb_dir:
        yMin = y0 + 1

    if 'U' in bomb_dir:
        yMax = y0 - 1

    x0 = xMin + xMax >> 1  # Bitwise operator equivalent to // 2, with lower prio than +
    y0 = yMin + yMax >> 1

    print(x0, y0)
    print(yMax, yMin, file=sys.stderr)

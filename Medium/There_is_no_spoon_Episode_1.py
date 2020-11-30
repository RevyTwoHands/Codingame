import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = [input() for _ in range(height)]



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(height):
    for j in range(width):
        if lines[i][j] == '0':
            x1=y1=x2=y2 = -1
            for k in range(j+1,width):
                if lines[i][k] == '0':
                    x1 = k
                    y1 = i
                    break
            for k in range(i+1, height):
                if lines[k][j] == '0':
                    x2 = j
                    y2 = k
                    break
            print(j, i, x1, y1, x2, y2)


# Three coordinates: a node, its right neighbor, its bottom neighbor


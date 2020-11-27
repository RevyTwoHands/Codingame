import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# first line (starts with a .)
print('.' + ' ' * (2 * (n - 1)) + '*')

# first triangle
for i in range(1, n):
    print(' ' * (2 * n - 1 - i) + '*' * (2 * i + 1))

# Or i can do this
# for i in range(n):
#    print("." * (i==0) + " " * (2*(n-1) - i + (i>0)) + "*" * (2*i+1))


# Second and Third triangles
for i in range(n):
    print(' ' * (n - 1 - i) + '*' * (2 * i + 1) + ' ' * (2 * (n - i) - 1) + '*' * (2 * i + 1))

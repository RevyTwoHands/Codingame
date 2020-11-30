import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# We're searching for prime numbers
print(n, file=sys.stderr)
for i in range(n//5 + 1):
    for j in range(i+1):
        x = (n - i*5 - j*2) / 3
        if x >= 0 and int(x)==x:
            print(i,j,int(x))


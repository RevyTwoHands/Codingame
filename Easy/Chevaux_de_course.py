import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
p = sorted([int(input()) for _ in range(n)])

pmin = min((p[i+1]-p[i] for i in range(n-1)))


print(pmin)

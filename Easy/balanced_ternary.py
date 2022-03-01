import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
out = ""
while n:
    out = "01T"[n % 3] + out
    n = (n + 1) // 3
print(out or "0")

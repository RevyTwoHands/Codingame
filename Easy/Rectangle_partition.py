import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def add_sides(table):
    delta = {}
    for i, mi in enumerate(table[:-1]):
        for mj in table[i + 1:]:
            d = mj - mi
            delta[d] = delta.get(d, 0) + 1
    return delta


w, h, count_x, count_y = [int(i) for i in input().split()]

x = [0] + [int(i) for i in input().split()] + [w]
y = [0] + [int(i) for i in input().split()] + [h]

res = 0

delta_x = add_sides(x)
delta_y = add_sides(y)

for d, nd in delta_x.items():
    res += nd * delta_y.get(d, 0)

print(res)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

grid = [input().split() for _ in range(n)]
print(grid, file=sys.stderr)


def value(grid, line):
    operation = grid[line][0]

    if grid[line][1][0] == '$':
        grid[line][1] = value(grid, int(grid[line][1][1:]))
    if grid[line][2][0] == '$':
        grid[line][2] = value(grid, int(grid[line][2][1:]))

    if operation == 'ADD':
        return str(int(grid[line][1]) + int(grid[line][2]))
    elif operation == 'SUB':
        return str(int(grid[line][1]) - int(grid[line][2]))
    elif operation == 'MULT':
        return str(int(grid[line][1]) * int(grid[line][2]))

    return grid[line][1]


for i in range(len(grid)):
    print(value(grid, i))
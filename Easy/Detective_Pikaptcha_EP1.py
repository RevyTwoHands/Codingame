dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
width, height = [int(i) for i in input().split()]


def number_of_adj(i, j, grid):
    global dirs, width, height
    if grid[i][j] == "#":
        return "#"
    else:
        res = 0
        for di, dj in dirs:
            ii, jj = i + di, j + dj
            res += (-1 < ii < height and -1 < jj < width and grid[ii][jj] != "#")
        return res


grid = [list(input()) for _ in range(height)]
for i in range(height):
    for j in range(width):
        print(number_of_adj(i, j, grid), end='')
    print()

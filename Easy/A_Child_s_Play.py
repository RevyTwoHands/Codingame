import sys


def move(x, y, room, dir, w, h):
    if dir == 'U' and x - 1 >= 0 and room[x - 1][y] == ".":
        return True
    elif dir == 'R' and y + 1 < w and room[x][y + 1] == ".":
        return True
    elif dir == 'D' and x + 1 < h and room[x + 1][y] == '.':
        return True
    elif dir == 'L' and y - 1 >= 0 and room[x][y - 1] == '.':
        return True
    return False


dirs = ['U', 'R', 'D', 'L']

w, h = [int(i) for i in input().split()]
n = int(input())
room = []
x = y = 0
for i in range(h):
    line = input()
    print(line, file=sys.stderr)
    if line.count('O') == 1:
        x = i
        y = line.index('O')
        line = line.replace('O', '.')
    room.append(line)

dir = 'U'
positions = [[x, y, dir]]
previous_x = 0
previous_y = 0
for i in range(n):
    previous_x = x
    previous_y = y
    for j in range(4):
        if move(x, y, room, dir, w, h):
            break
        else:
            dir = dirs[(dirs.index(dir) + 1) % 4]
    if dir == 'U':
        x -= 1
    elif dir == 'R':
        y += 1
    elif dir == 'D':
        x += 1
    else:
        y -= 1
    if [x, y, dir] in positions:
        a = positions.index([x, y, dir])

        if a == 0:
            loop = positions[n % (i - a + 1)]
        else:
            if positions[a - 1][0] == previous_x and positions[a - 1][1] == previous_y:
                a = a - 1
            positions = positions[a:-1]
            loop = positions[(n - i) % len(positions)]
            print(positions, file=sys.stderr)
        print(loop[1], loop[0])
        exit()
    positions.append([x, y, dir])
print(positions[-1][1], positions[-1][0])

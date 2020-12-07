w, h = [int(i) for i in input().split()]
lines = [input() for i in range(h)]

names = lines[0].split()
values = lines[-1].split()
order = lines[0].split()

for line in lines[1:-1]:
    for i in range(1, len(line), 3):
        if line[i] == '-':
            order[(i-1)//3], order[(i+2)//3] = order[(i+2)//3], order[(i-1)//3]

for name in names:
    print(name + values[order.index(name)])

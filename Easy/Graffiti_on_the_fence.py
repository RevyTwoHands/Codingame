length = int(input())
nb_reports = int(input())
reports = sorted([list(map(int, input().split())) for _ in range(nb_reports)])

not_painted = []
start, finish = 0, 0
for s, f in reports:
    if finish < s:
        not_painted.append((start, s))
    if finish < f:
        start = f
        finish = f

if finish < length:
    not_painted.append((finish, length))

if not_painted:
    for np in not_painted:
        print(*np)
else:
    print("All painted")

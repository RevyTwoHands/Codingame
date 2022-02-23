from itertools import combinations

m = int(input())
n = int(input())
bars = [int(i) for i in input().split()]
M = 0
res = []

for i in range(1, n + 1):
    for j in combinations(bars, i):
        if sum(j) > M and sum(j) <= m:
            M = sum(j)
            res = j
print(*res)
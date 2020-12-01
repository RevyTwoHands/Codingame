import sys
import math

n = int(input())
lst = []
dic_winners = {i: [] for i in range(1, n + 1)}
for i in range(n):
    inputs = input().split()
    lst.append((int(inputs[0]), inputs[1]))

dic = {'R': 'CL', 'P': 'RS', 'C': 'PL', 'L': 'SP', 'S': 'CR'}

while len(lst) > 1:
    new_games = []
    for p1, p2 in zip(lst[::2], lst[1::2]):
        n1, n2 = p1[0], p2[0]
        h1, h2 = p1[1], p2[1]
        dic_winners[n1] += [n2]
        dic_winners[n2] += [n1]
        new_games += [p1] if h2 in dic[h1] else [p2] if h1 in dic[h2] else [[p1], [p2]][n1 > n2]
    lst = new_games

print(lst[0][0])
print(*dic_winners[lst[0][0]])

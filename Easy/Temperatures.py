import math

tmp_neg = -math.inf
tmp_pos = math.inf

n = int(input())  # the number of temperatures to analyse

lst = [int(e) for e in input().split()]

for e in lst:
    if e >= 0:
        tmp_pos = min(tmp_pos, e)
    else:
        tmp_neg = max(tmp_neg, e)

if len(lst) > 0:
    print([tmp_neg, tmp_pos][abs(tmp_neg) >= tmp_pos])
else:
    print(0)


r_1 = int(input())

def river(x):
    return x + sum([int(e) for e in str(x)])

is_possible = 'NO'

for i in range(r_1):
    if river(i) == r_1:
        is_possible = 'YES'
        break

print(is_possible)

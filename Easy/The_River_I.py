a = int(input())
b = int(input())


def river(k):
    return k + sum([int(e) for e in str(k)])


while a != b:
    (a, b) = [(a, river(b)), (river(a), b)][a < b]

print(a)
